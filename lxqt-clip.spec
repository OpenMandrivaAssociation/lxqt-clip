Name:         lxqt-clip
Version:      2.5.0
Release:      1
Summary:      LXQt clipboard history applet
License:      GPLv2+
Group:        Graphical desktop/KDE
URL:          https://lxqt-project.org/
Source0:      https://github.com/lxqt/lxqt-clip/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: cmake
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: pkgconfig(x11)

%description
Lightweight clipboard history applet by LXQt for X11 and Wayland.

Based on original Qlipper https://github.com/pvanek/qlipper.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license COPYING
%doc CHANGELOG README*
%{_bindir}/lxqt-clip
%{_sysconfdir}/xdg/autostart/lxqt-clip-autostart.desktop
%{_datadir}/applications/lxqt-clip.desktop
%{_datadir}/lxqt/translations/lxqt-clip/
%{_iconsdir}/hicolor/*x*/apps/lxqt-clip.png

