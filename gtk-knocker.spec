Summary:	Simple port scanner using GTK
Summary(pl.UTF-8):	Prosty skaner portów używający GTK
Name:		gtk-knocker
Version:	0.6.6
Release:	3
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/knocker/%{name}-%{version}.tar.gz
# Source0-md5:	435f5bbd4c51d751336206f409e882cf
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-am15.patch
Patch1:		%{name}-gcc33.patch
URL:		http://knocker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knocker is a simple, versatile, and easy-to-use TCP security port
scanner written in C, using GTK.

%description -l pl.UTF-8
Knocker jest prostym, uniwersalnym i łatwym w użyciu skanerem portów
używającym GTK.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS BUGS TO-DO
%attr(755,root,root) %{_bindir}/gtk-knocker
%{_desktopdir}/gtk-knocker.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
