from pathlib import Path
from rdfx.rdfx import merge

from rdfx.persistence_systems import File

def test_merge_directory():
    output_format = 'ttl'
    input_dir = Path(Path(__file__).parent / "data")
    files = [file for file in input_dir.glob("*.*")]
    output_file = input_dir/f'merged.{output_format}'
    ps = File(output_file, output_format)
    merge(files, ps)
    assert(output_file.exists())
    # delete the file
    output_file.unlink()
