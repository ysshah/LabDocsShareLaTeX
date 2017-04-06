import os
import subprocess

LABS = ['AFM', 'ATM', 'CO2', 'MNO', 'MOT', 'NMR', 'OPT', 'QIE', 'BMC', 'OTZ',
    'COM', 'MUO', 'GMA', 'BRA', 'RUT', 'HAL', 'LLS', 'NLD', 'JOS', 'SHE']

# Command to install LaTeX
install_cmd = ('sudo apt-get update && sudo apt-get install '
    '--no-install-recommends texlive-fonts-recommended '
    'texlive-latex-extra texlive-fonts-extra texlive-latex-recommended '
    'dvipng')

# Retrieve changed files in the latest git push
diff_cmd = 'git diff --name-only ' + os.environ['TRAVIS_COMMIT_RANGE']
changed_files = subprocess.check_output(
    diff_cmd.split()).decode('utf-8').split('\n')


if 'lab.cls' in changed_files:
    # If lab.cls is changed, rebuild all PDFs
    # labs_to_rebuild = LABS
    labs_to_rebuild = ['OPT']
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

    for lab in labs_to_rebuild:
        print 'Rebuilding', lab
        build_cmd = 'cd {} && pdflatex -output-directory build {}.tex'.format(lab, lab)
        subprocess.call(build_cmd.split())

    subprocess.call('ls')
    subprocess.call(['ls', 'build'])
