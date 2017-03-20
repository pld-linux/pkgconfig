Summary:	A tool for determining compilation options
Summary(pl.UTF-8):	Narzędzie do ustalania opcji kompilacji
Summary(pt_BR.UTF-8):	Ferramenta para determinar opções de compilação
Summary(ru.UTF-8):	Инструмент для определения опций компиляции
Summary(uk.UTF-8):	Інструмент для визначення опцій компіляції
Name:		pkgconfig
Version:	0.29.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz
# Source0-md5:	f6e931e319531b736fadc017f470e68a
URL:		https://pkgconfig.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	libtool >= 2:2.2
Requires:	glib2 >= 1:2.16
Provides:	pkg-config = %{version}-%{release}
Provides:	pkgconfig(pkg-config) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
pkgconfig is a tool for determining compilation options. For each
required library it reads a configuration file installed in a standard
option and ouputs the necessary compiler and linker flags.

%description -l pl.UTF-8
pkgconfig jest programem używanym do uzyskiwania informacji o
zainstalowanych w systemie bibliotekach.

%description -l pt_BR.UTF-8
A ferramenta pkgconfig determina opções de compilação. Para cada
biblioteca requerida a ferramenta lê seus arquivos de configuração e
emite as opções necessárias para o compilador e ligador.

%description -l ru.UTF-8
pkgconfig - это инструмент для определения опций компиляции. Для
каждой необходимой библиотеки он считывает конфигурационный файл и
выдает необходимые флаги компилятора и линкера.

%description -l uk.UTF-8
pkgconfig - це інструмент для визначення опцій компіляції. Для кожної
необхідної бібліотеки він зчитує конфігураційний файл та видає
потрібні флаги компілятора та лінкера.

%prep
%setup -q -n pkg-config-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
GLIB_CFLAGS="-I/usr/include/glib-2.0 -I%{_libdir}/glib-2.0/include" \
GLIB_LIBS="-lglib-2.0" \
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4dir=%{_aclocaldir}

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/pkg-config/pkg-config-guide.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README pkg-config-guide.html
%attr(755,root,root) %{_bindir}/pkg-config
%attr(755,root,root) %{_bindir}/*-pld-linux-gnu*-pkg-config
%{_aclocaldir}/pkg.m4
%{_mandir}/man1/pkg-config.1*
