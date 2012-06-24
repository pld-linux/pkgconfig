Summary:	A tool for determining compilation options
Summary(pl):	Narz�dzie do ustalania opcji kompilacji
Summary(pt_BR):	Ferramenta para determinar op��es de compila��o
Summary(ru):	���������� ��� ����������� ����� ����������
Summary(uk):	���������� ��� ���������� ��æ� ���Ц��æ�
Name:		pkgconfig
Version:	0.17
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a7d9844b3d89af68388f9fa996634322
# it's not directory, don't add /
URL:		http://www.freedesktop.org/wiki/Software_2fpkgconfig
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# NOTE: don't try tu use system glib-1.2.x and popt - it BREAKS things.
# See http://bugzilla.gnome.org/show_bug.cgi?id=63208.
# Always use internal (modified) copies of glib/popt) --misiek

%description
pkgconfig is a tool for determining compilation options. For each
required library it reads a configuration file installed in a standard
option and ouputs the necessary compiler and linker flags.

%description -l pl
pkgconfig jest programem u�ywanym do uzyskiwania informacji o
zainstalowanych w systemie bibliotekach.

%description -l pt_BR
A ferramenta pkgconfig determina op��es de compila��o. Para cada
biblioteca requerida a ferramenta l� seus arquivos de configura��o e
emite as op��es necess�rias para o compilador e ligador.

%description -l ru
pkgconfig - ��� ���������� ��� ����������� ����� ����������. ���
������ ����������� ���������� �� ��������� ���������������� ���� �
������ ����������� ����� ����������� � �������.

%description -l uk
pkgconfig - �� ���������� ��� ���������� ��æ� ���Ц��æ�. ��� ����ϧ
����Ȧ��ϧ ¦�̦����� צ� ����դ ���Ʀ����æ���� ���� �� �����
���Ҧ�Φ ����� ���Ц������ �� ̦�����.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
cp -f /usr/share/automake/config.* glib-1.2.8
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
