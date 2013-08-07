Name:     setbranding
Version:  1.0.0
Release:  alt1

Summary:  Script for manipulation ALT Linux branding packages
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/setbranding
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source:   setbranding

Requires:  apt

%description
Script for manipulation ALT Linux branding (distribution design profile)
packages. You can show installed branding packages and switch to other
branding.

%install
install -Dm755 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Wed Aug 07 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus

