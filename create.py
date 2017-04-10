import os
import subprocess

LABS = ['AFM', 'ATM', 'CO2', 'MNO', 'MOT', 'NMR', 'OPT', 'QIE', 'BMC', 'OTZ',
    'COM', 'MUO', 'GMA', 'BRA', 'RUT', 'HAL', 'LLS', 'NLD', 'JOS', 'SHE']

SITE = '0bc915fe-2126-4798-9621-fdf6aa78ed57'

# Retrieve changed files in the latest git push
diff_cmd = 'git diff --name-only ' + os.environ['TRAVIS_COMMIT_RANGE']
changed_files = subprocess.check_output(
    diff_cmd.split()).decode('utf-8').split('\n')


if 'lab.cls' in changed_files:
    # If lab.cls is changed, rebuild all PDFs
    labs_to_rebuild = [lab for lab in LABS if os.path.exists(lab)]
else:
    # Otherwise, only rebuild PDFs that have changed files
    labs_to_rebuild = set()
    for file in changed_files:
        lab = file.split('/')[0]
        if lab in LABS:
            labs_to_rebuild.add(lab)

if len(labs_to_rebuild) > 0:

    # Make a 'build' directory
    subprocess.call(['mkdir', 'build'])

    # Get the base directory for pointing to specific files
    base_dir = os.environ['TRAVIS_BUILD_DIR']

    for lab in labs_to_rebuild:
        print 'Rebuilding', lab
        build_cmd = 'cd {}/{} && latexmk -outdir=../build -pdf {}'
        subprocess.call(build_cmd.format(base_dir, lab, lab), shell=True)

        # Sync the PDF to Physics lab website
        sync_cmd = ("rsync -vz --ipv4 --progress -e 'ssh -p 2222' "
            "{}/build/{}.pdf --temp-dir=~/tmp/ "
            "live.{}@appserver.live.{}.drush.in:files/writeups/")
        subprocess.call(sync_cmd.format(base_dir, lab, SITE, SITE), shell=True)

else:
    print 'No labs to rebuild.'
