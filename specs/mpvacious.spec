Name:       mpvacious
Version:    0.41
Release:    1%{?dist}
Summary:    Adds mpv keybindings to create Anki cards from movies and TV shows

License:    GPL-3.0-or-later
URL:        https://github.com/Ajatt-Tools/mpvacious
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   mpv curl gawk
Recommends: ffmpeg
Suggests:   wl-clipboard xclip

%description
Adds mpv keybindings to create Anki cards from movies and TV shows.

%prep
%autosetup

%install
mkdir -p "%{buildroot}%{_sysconfdir}/mpv/scripts"
find . -type f -iname "*.lua" -exec install -Dm644 "{}" "%{buildroot}%{_datadir}/mpv/scripts/%{name}/{}" \;
ln -sf "%{_datadir}/mpv/scripts/%{name}" "%{buildroot}%{_sysconfdir}/mpv/scripts/"
install -Dm644 .github/RELEASE/subs2srs.conf "%{buildroot}%{_sysconfdir}/mpv/script-opts/subs2srs.conf"

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/mpv/script-opts/subs2srs.conf
%dir %{_datadir}/mpv
%dir %{_datadir}/mpv/scripts
%{_datadir}/mpv/scripts/mpvacious/
%dir %{_sysconfdir}/mpv/scripts
%{_sysconfdir}/mpv/scripts/%{name}

%changelog
%autochangelog
