Summary:	Simple port scanner using GTK
Summary(pl):	Prosty skaner portów uzywajacy GTK
Name:		gtk-knocker
Version:	0.6.6
Release:	1
License:	GPL
Group:		Networking/Utilities
URL:		http://knocker.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/knocker/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2.0

%description
Knocker is a simple, versatile, and easy-to-use TCP security port
scanner written in C, using GTK.

%description -l pl
Knocker jest prostym, uniwersalnym i ³atwym w u¿yciu skanerem portów
u¿ywaj±cym GTK.

%prep
%setup -q

%build
./configure

%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/gtk-knocker	$RPM_BUILD_ROOT%{_bindir}
install docs/gtk-knocker.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-knocker
%doc ChangeLog AUTHORS BUGS TO-DO
%{_mandir}/man1/*
