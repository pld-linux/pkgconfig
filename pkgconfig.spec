Summary: A tool for memory profiling and leak detection.
Name: pkgconfig
Version: 0.4.0
Release: 2
Epoch: 1
License: GPL
Group: Development/Tools
Source: http://download.sourceforge.net/pkgconfig/pkgconfig-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
pkgconfig is a tool for determining compilation options.
For each required library it reads a configuration file installed
in a standard option and ouputs the necessary compiler and linker
flags.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig
strip $RPM_BUILD_ROOT%{_prefix}/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/bin/*
%{_prefix}/lib/pkgconfig

%changelog
* Thu Dec 14 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Wed Oct 04 2000 Owen Taylor <otaylor@redhat.com>
- Initial package
