import pathlib, subprocess, sys

def main():
    src = pathlib.Path("index.html")
    if not src.exists():
        sys.exit("index.html missing")
    patch_file = pathlib.Path("/tmp/update.patch")
    base = pathlib.Path("/tmp/base.html")
    base.write_bytes(src.read_bytes().replace(b"\r\n", b"\n"))
    r = subprocess.run(["patch", "--no-backup-if-mismatch", "-p1", str(base), "-i", str(patch_file)],
                       capture_output=True, text=True)
    print(r.stdout)
    print(r.stderr)
    if r.returncode != 0:
        sys.exit("patch failed")
    data = base.read_bytes()
    src.write_bytes(data)
    print("index.html ->", len(data), "bytes;", b"data-catalog" in data)

main()
