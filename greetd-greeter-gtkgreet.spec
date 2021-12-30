Summary:	GTK greeter for greetd
Name:		greetd-greeter-gtkgreet
Version:	0.7
Release:	1
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~kennylevinsen/gtkgreet/archive/%{version}.tar.gz
# Source0-md5:	f027ae4d4e63130cf349fdecb96afbad
URL:		https://git.sr.ht/~kennylevinsen/gtkgreet
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-layer-shell-devel
BuildRequires:	json-c-devel
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc >= 1.9.7
Requires:	greetd
Suggests:	cage
Provides:	greetd(greeter)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK based greeter for greetd, to be run under cage or similar.

%prep
%setup -q -n gtkgreet-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/greetd

%ninja_install -C build

echo sh > $RPM_BUILD_ROOT/etc/greetd/environments

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%config(noreplace) %verify(not md5 mtime size) /etc/greetd/environments
%attr(755,root,root) %{_bindir}/gtkgreet
%{_mandir}/man1/gtkgreet.1*
