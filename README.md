# package.json parser

A script to fetch information on the dependencies of your JavaScript projects and output that to a CSV file.

## Usage

1. Install Python - `brew install python` on a Mac
1. `./parse_package_json.py <source folder> <output file>`

## Options

`source folder` - Root folder to look for package.json files in. This is recursive, but ignores your dependecies (i.e. the contents of `node_modules`)
`output file` - Where to write the results to

Both are mandatory.
