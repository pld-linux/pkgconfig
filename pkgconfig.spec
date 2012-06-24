# TODO: system popt, system glib2 with bootstrap bcond?
Summary:	A tool for determining compilation options
Summary(pl.UTF-8):	Narzędzie do ustalania opcji kompilacji
Summary(pt_BR.UTF-8):	Ferramenta para determinar opções de compilação
Summary(ru.UTF-8):	Инструмент для определения опций компиляции
Summary(uk.UTF-8):	Інструмент для визначення опцій компіляції
Name:		pkgconfig
Version:	0.25
Release:	4
Epoch:		1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz
# Source0-md5:	a3270bab3f4b69b7dc6dbdacbcae9745
Patch0:		%{name}-ac.patch
URL:		http://pkgconfig.freedesktop.org/wiki/
BuildRequires:	automake
Provides:	pkg-config = %{version}-%{release}
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
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
cp -f /usr/share/automake/config.* glib-1.2.10
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4dir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README pkg-config-guide.html
%attr(755,root,root) %{_bindir}/pkg-config
%{_aclocaldir}/pkg.m4
%{_mandir}/man1/pkg-config.1*
