#!/usr/bin/env python

import csv, json, fnmatch, os
from sys import argv

script, rootFolder, outputFile, options = argv

excludes = ['node_modules']
matches = []
for root, dirnames, filenames in os.walk(rootFolder, topdown=True):
    dirnames[:] = [d for d in dirnames if d not in excludes]
    for filename in fnmatch.filter(filenames, 'package.json'):
        matches.append(os.path.join(root, filename))

print('Found [' + str(len(matches)) + '] package.json files')

packages = {}


def add_deps(deps, f):
    for dep in iter(deps):
        module_package_json = json.load(open(os.path.dirname(f) + '/node_modules/' + dep + '/package.json'))
        packages[dep] = {
            'version': deps[dep],
            'license': module_package_json['license'] if 'license' in module_package_json else 'unknown',
            'description': module_package_json['description'] if 'description' in module_package_json else 'none'
        }

if len(matches) > 0:
    output = csv.writer(open(outputFile, 'wb'))
    output.writerow(['Package Name', 'Version', 'License', 'Description'])

    for match in matches:
        packageJson = json.load(open(match))
        if 'dependencies' in packageJson:
            print(packageJson['name'] + ' has ' + str(len(packageJson['dependencies'])) + ' dependencies')
            add_deps(packageJson['dependencies'], match)
        if ('devDependencies' in packageJson) & ('dev' in options):
            print(packageJson['name'] + ' has ' + str(len(packageJson['devDependencies'])) + ' devDependencies')
            add_deps(packageJson['devDependencies'], match)

for package in iter(packages):
    output.writerow([package, packages[package]['version'], packages[package]['license'], packages[package]['description']])
