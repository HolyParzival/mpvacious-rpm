#!/bin/bash

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 FILE"
    exit 1
fi

spec=$1

github_url=$(awk '/^URL:/ {print $2}' "$spec")
package_name=$(awk '/^Name:/ {print $2}' "$spec")
current_version=$(awk '/^Version:/ {print $2}' "$spec")

owner=$(echo "$github_url" | awk -F/ '{print $4}')
repo=$(echo "$github_url" | awk -F/ '{print $5}')
latest_version=$(curl -s "https://api.github.com/repos/$owner/$repo/releases/latest" | jq -r '.tag_name' | sed 's/^v//')

if [[ "$current_version" == "$latest_version" ]]; then
  echo "No new version available."
  exit 0
fi

echo "New $package_name version available: $latest_version"
echo "Updating $spec and pushing new tag..."

release=1
release_string="$release%{?dist}"
tag="$package_name-$latest_version-$release"

sed -i "/^Version:/ s/$current_version/$latest_version/" "$spec"
sed -i "s/^\(Release:\s*\).*/\1$release_string/" "$spec"

git diff "$spec"
git add "$spec"
git commit -m "Update $package_name to $latest_version"
git tag "$tag"
git push origin
git push origin tag "$tag"
