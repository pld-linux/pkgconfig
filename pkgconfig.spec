Summary:	A tool for determining compilation options
Summary(pl):	Narzêdzie do ustalania opcji kompilacji
Name:		pkgconfig
Version:	0.11.0
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://www.freedesktop.org/software/pkgconfig/releases/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
URL:		http://www.freedesktop.org/software/pkgconfig/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkgconfig is a tool for determining compilation options. For each
required library it reads a configuration file installed in a standard
option and ouputs the necessary compiler and linker flags.

%description -l pl
pkgconfig jest programen uzywanym do uzyskiwania informacji
o zainstalowanych w systemie bibliotekach.

%prep
%setup -q
# This patch BREAKS things. See http://bugzilla.gnome.org/show_bug.cgi?id=63208.
# Always use internal (modified) copies of glib/popt) --misiek
# %patch -p1

%build
#rm -f missing
#libtoolize --copy --force
#aclocal
#autoconf
#automake -a -c
#cd glib-*
#  libtoolize --copy --force
#  aclocal
#  autoconf
#cd ..
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4dir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}
%{_aclocaldir}/*
%{_mandir}/man1/*
