import shutil
from pathlib import Path

import click
import pandas as pd
import yaml
from click import confirm
from PIL import Image
from tqdm import tqdm

from brainways.project.brainways_subject import BrainwaysSubject
from brainways.utils.io_utils.readers.qupath_reader import QupathReader


@click.command()
@click.option(
    "--input",
    type=Path,
    required=True,
    help=(
        "Input subject file / directory of subject files to create registration model"
        " training data for."
    ),
)
@click.option("--output", type=Path, required=True, help="Output directory.")
def create_reg_model_data(input: Path, output: Path):
    if output.exists():
        confirm("Output directory already exists, overwrite?", abort=True)
        shutil.rmtree(output)

    if (input / "brainways.bin").exists():
        paths = [input]
    else:
        paths = sorted(list(input.rglob("*.bin")))

    labels = []
    metadata = None
    output_images_dir = output / "images"
    output.mkdir()
    output_images_dir.mkdir()
    for subject_path in tqdm(paths):
        subject = BrainwaysSubject.open(subject_path)
        if metadata is None:
            subject.load_atlas(load_volumes=False)
            metadata = {
                "atlas": subject.settings.atlas,
                "ap_size": subject.atlas.brainglobe_atlas.shape[0],
                "si_size": subject.atlas.brainglobe_atlas.shape[1],
                "lr_size": subject.atlas.brainglobe_atlas.shape[2],
            }
            with open(output / "metadata.yaml", "w") as outfile:
                yaml.dump(metadata, outfile, default_flow_style=False)
        if subject.settings.atlas != metadata["atlas"]:
            print(
                f"subject {subject_path.parent.name} has a different atlas"
                f" {subject.settings.atlas} (expected  {metadata['atlas']})"
            )
            continue
        for document in tqdm(
            subject.documents, desc=subject_path.parent.name, leave=False
        ):
            ap = None
            rot_frontal = None
            rot_horizontal = None
            rot_sagittal = None
            hemisphere = None
            if not document.ignore:
                ap = document.params.atlas.ap
                rot_horizontal = document.params.atlas.rot_horizontal
                rot_sagittal = document.params.atlas.rot_sagittal
                hemisphere = document.params.atlas.hemisphere
                if document.params.affine is not None:
                    rot_frontal = -document.params.affine.angle

            reader = QupathReader(document.path.filename)
            reader.set_scene(document.path.scene)
            for channel_index, channel in enumerate(reader.channel_names):
                output_image_filename = subject_path.parent.relative_to(input) / (
                    Path(str(document.path.with_channel(channel_index))).name + ".tif"
                )
                labels.append(
                    {
                        "filename": str(output_image_filename),
                        "animal_id": Path(subject.subject_path).name,
                        "image_id": str(document.path),
                        "ap": ap,
                        "rot_frontal": rot_frontal,
                        "rot_horizontal": rot_horizontal,
                        "rot_sagittal": rot_sagittal,
                        "valid": "no" if document.ignore else "yes",
                        "hemisphere": hemisphere,
                        "channel": channel,
                    }
                )
                output_image_path = output_images_dir / output_image_filename
                output_image_path.parent.mkdir(parents=True, exist_ok=True)
                image = reader.get_thumbnail(
                    target_size=document.lowres_image_size, channel=channel_index
                )
                Image.fromarray(image).save(output_image_path)

    # write labels
    pd.DataFrame(labels).to_csv(output / "labels.csv", index=False)
