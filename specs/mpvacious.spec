%global     debug_package %{nil}

Name:       mpvacious
Version:    0.39
Release:    1%{?dist}
Summary:    Semi-automatic subs2srs for mpv

License:    GPL-3.0-or-later
URL:        https://github.com/Ajatt-Tools/mpvacious
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   mpv

%description
mpvacious is your semi-automatic subs2srs for mpv.
It supports multiple workflows and allows you to quickly
create Anki cards while watching your favorite TV show.

%prep
%autosetup

%install
find . -type f -iname "*.lua" -exec install -Dm644 "{}" "%{buildroot}%{_datadir}/mpv/scripts/%{name}/{}" \;
install -Dm644 .github/RELEASE/subs2srs.conf "%{buildroot}%{_datadir}/mpv/script-opts/subs2srs.conf"

%files
%dir %{_datadir}/mpv
%dir %{_datadir}/mpv/scripts
%dir %{_datadir}/mpv/script-opts
%{_datadir}/mpv/scripts/mpvacious
%{_datadir}/mpv/script-opts/subs2srs.conf
%license LICENSE
%doc README.md

%changelog
%autochangelog
