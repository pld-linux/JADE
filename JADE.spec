Summary:	Jade -- DSSSL parser
Summary(pl):	Jade  -- parser DSSSL
%define		jade jade
%define		jadever 1.2.1
%define		spver 1.3.1
Name:		%{jade}
Version:	%{jadever}
Release:	2
Serial:		6
Vendor:		James Clark
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Copyright:	(C) 1997 James Clark (free)
Source0:	ftp://ftp.jclark.com/pub/jade/%{name}-%{version}.tar.gz
Source1:	unicode.cat
Source2:	dsssl.cat
Source3:	sp-html.cat
Provides:	dssslparser
URL:		http://www.jclark.com/jade/
Prereq:		/usr/sbin/install-catalog
Requires:	sgml-common
Requires:	sp
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Jade (James' DSSSL Engine) is an implementation of the DSSSL style language. 

%description -l pl
Jade (James' DSSSL Engine) jest implementacj± parsera DSSSL.

%package -n sp
Summary:	SP -- parser and tools for SGML
Summary(pl):	SP -- parser and tools for SGML
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
URL:		http://www.jclark.com/sp/
Prereq:		/usr/sbin/install-catalog
Provides:	sgmlparser
Requires:	sgml-common
Version:	%{spver}_%{jadever}

%description -n sp
SGML parser called sp (replacement of sgmls).

%description -n sp -l pl
Parser SGML (bêd±cy nastêpc± pisanego w C sgmls) oraz narzêdzia
do normalizacji SGML-a (sgmlnorm), konwersji tego¿ do XMLa (sx).

%prep
%setup -q  

%build
%configure \
	--prefix=/usr \
	--enable-shared \
	--with-gnu-ld \
	--sharedstatedir=%{_datadir} \
	--enable-default-catalog=%{_datadir}/sgml/CATALOG  \
	--enable-mif

make  

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/sgml/{dsssl/jade,html}
	$RPM_BUILD_ROOT%{_libdir}

make -f Makefile install prefix="$RPM_BUILD_ROOT/usr"

cp -ar pubtext/* $RPM_BUILD_ROOT%{_datadir}/sgml/html
cp -ar unicode $RPM_BUILD_ROOT%{_datadir}/sgml

install $RPM_SOURCE_DIR/{dsssl,sp-html,unicode}.cat \
    $RPM_BUILD_ROOT/usr/share/sgml

cp -ar dsssl/catalog $RPM_BUILD_ROOT%{_datadir}/sgml/dsssl/jade
cp -ar dsssl/dsssl.dtd dsssl/style-sheet.dtd dsssl/fot.dtd \
	$RPM_BUILD_ROOT%{_datadir}/sgml/dsssl/jade

strip $RPM_BUILD_ROOT%{_bindir}/*

%post
/usr/sbin/install-catalog --install dsssl  --version  %{jadever}-%{release}

%preun
/usr/sbin/install-catalog --remove dsssl   --version  %{jadever}-%{release}

%post -n sp
/usr/sbin/install-catalog --install sp-html --version %{spver}-%{release}
/usr/sbin/install-catalog --install unicode --version %{spver}-%{release}

%preun -n sp
/usr/sbin/install-catalog --remove sp-html --version %{spver}-%{release} 
/usr/sbin/install-catalog --remove unicode --version %{spver}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc jadedoc/ dsssl/ README COPYING VERSION

%attr(755,root,root) %{_bindir}/jade
%attr(755,root,root) %{_libdir}/libstyle.so*
%attr(755,root,root) %{_libdir}/libgrove.so*
%attr(755,root,root) %{_libdir}/libspgrove.so*

%config {_datadir}/sgml/dsssl.cat
{_datadir}/sgml/dsssl/*

%files -n sp
%defattr(644,root,root,755)
%doc doc/

%attr(755,root,root) %{_bindir}/s*
%attr(755,root,root) %{_bindir}/nsgmls
%attr(755,root,root) %{_libdir}/libsp.so*

%config {_datadir}/sgml/sp-html.cat
{_datadir}/sgml/html

%config {_datadir}/sgml/unicode.cat
{_datadir}/sgml/unicode

%changelog
* Thu Oct 26 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
  [1.2.1-1] 
- upgrade to 1.2.1 (with dynamic libraries -- changes in %files part)
- corrects to *.cat files (not dynamicaly generated). 
- (I`m not sure if we ought to include *.la files -- not included).  
- added --enable-mif (but it does`t working ;-( 
- some cosmetic changes in spec: (new group, new prereq) 
- simplifications in %post{un}

* Thu Sep 26 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
  [1_2-4]
- updated new version
- added  -Dsig_atomic_t=int to make (against glibc-2.x --
  required in glibc-2.0.93 but its help in 2.0.7 too)

* Thu Sep 10 1998 Wojtek ¦lusarczyk <wojtek@SHADOW.EU.ORG>
  [1_1_1-3]
- patch against glibc 2.0.93  (quick & dirty)   (not nessessary in 1_2)

* Mon Sep 07 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
  [1_1_1-2]
- added Polish .spec tranlation
- more detailed .spec
- separated to: jade, and sp  packages
- based od Mark Gallasi works ftp://ftp.cygnus.com/pub/home/rozalia/docware
