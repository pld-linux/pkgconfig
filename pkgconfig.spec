Summary:	A tool for determining compilation options
Summary(pl):	NarzЙdzie do ustalania opcji kompilacji
Summary(pt_BR):	Ferramenta para determinar opГУes de compilaГЦo
Summary(ru):	Инструмент для определения опций компиляции
Summary(uk):	╤нструмент для визначення опц╕й комп╕ляц╕╖
Name:		pkgconfig
Version:	0.14.0
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://www.freedesktop.org/software/pkgconfig/releases/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
URL:		http://www.freedesktop.org/software/pkgconfig/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkgconfig is a tool for determining compilation options. For each
required library it reads a configuration file installed in a standard
option and ouputs the necessary compiler and linker flags.

%description -l pl
pkgconfig jest programen uzywanym do uzyskiwania informacji o
zainstalowanych w systemie bibliotekach.

%description -l pt_BR
A ferramenta pkgconfig determina opГУes de compilaГЦo. Para cada
biblioteca requerida a ferramenta lЙ seus arquivos de configuraГЦo e
emite as opГУes necessАrias para o compilador e ligador.

%description -l ru
pkgconfig - это инструмент для определения опций компиляции. Для
каждой необходимой библиотеки он считывает конфигурационный файл и
выдает необходимые флаги компилятора и линкера.

%description -l uk
pkgconfig - це ╕нструмент для визначення опц╕й комп╕ляц╕╖. Для кожно╖
необх╕дно╖ б╕бл╕отеки в╕н зчиту╓ конф╕гурац╕йний файл та вида╓
потр╕бн╕ флаги комп╕лятора та л╕нкера.

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
