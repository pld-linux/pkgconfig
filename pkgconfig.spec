Summary:	A tool for determining compilation options
Summary(pl.UTF-8):   Narzędzie do ustalania opcji kompilacji
Summary(pt_BR.UTF-8):   Ferramenta para determinar opções de compilação
Summary(ru.UTF-8):   Инструмент для определения опций компиляции
Summary(uk.UTF-8):   Інструмент для визначення опцій компіляції
Name:		pkgconfig
Version:	0.21
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz
# Source0-md5:	476f45fab1504aac6697aa7785f0ab91
URL:		http://pkgconfig.freedesktop.org/wiki/
BuildRequires:	automake
Provides:	pkg-config = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# NOTE: don't try tu use system glib-1.2.x and popt - it BREAKS things.
# See http://bugzilla.gnome.org/show_bug.cgi?id=63208.
# Always use internal (modified) copies of glib/popt) --misiek

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
cp -f /usr/share/automake/config.* .
cp -f /usr/share/automake/config.* glib-1.2.8
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*
%{_mandir}/man1/*
