Summary:     Jade -- DSSSL parser
%define      jade jade
%define      jadever 1.2.1
%define      spver 1.3.1
Name: 	     %{jade}
Version:     %{jadever}
Release:     1d
Serial:	     6
Vendor:      James Clark
Group:       Applications/Publishing/SGML
Group(pl):   Aplikacje/Publikowanie/SGML
URL: 	     http://www.jclark.com/jade/
Source:	     ftp://ftp.jclark.com/pub/jade/%{name}-%{version}.tar.gz
Source1:     unicode.cat
Source2:     dsssl.cat
Source3:     sp-html.cat
Copyright:   (C) 1997 James Clark (free)
Provides:    dssslparser
Prereq:	     /usr/sbin/install-catalog
Requires:    sgml-common
Requires:    sp
BuildRoot:   /tmp/%{name}-%{version}-root
Summary(pl): Jade  -- parser DSSSL

%description
Jade (James' DSSSL Engine) is an implementation of the DSSSL style language. 

%description -l pl
Jade (James' DSSSL Engine) jest implementacj± parsera DSSSL.

%package -n sp
Summary:     SP -- parser and tools for SGML
Group:       Applications/Publishing/SGML
Group(pl):   Aplikacje/Publikowanie/SGML
URL: 	     http://www.jclark.com/sp/
Prereq:	     /usr/sbin/install-catalog
Provides:    sgmlparser
Requires:    sgml-common
Version:     %{spver}_%{jadever}
Summary(pl): SP -- parser and tools for SGML

%description -n sp
SGML parser called sp (replacement of sgmls).

%description -n sp -l pl
Parser SGML (bêd±cy nastêpc± pisanego w C sgmls) oraz narzêdzia
do normalizacji SGML-a (sgmlnorm), konwersji tego¿ do XMLa (sx).

%prep

%setup -q  

%build

./configure %{buildarch}-unknown-`echo %{buildos} | tr A-Z a-z` \
 --enable-shared --with-gnu-ld --prefix=/usr --sharedstatedir=/usr/share \
 --enable-default-catalog=/usr/share/sgml/CATALOG  \
 --enable-mif

make  

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/share/sgml/{dsssl/jade,html}
install -d $RPM_BUILD_ROOT/usr/lib

make -f Makefile install prefix="$RPM_BUILD_ROOT/usr"

cp -ar pubtext/* $RPM_BUILD_ROOT/usr/share/sgml/html
cp -ar unicode $RPM_BUILD_ROOT/usr/share/sgml

install $RPM_SOURCE_DIR/{dsssl,sp-html,unicode}.cat \
    $RPM_BUILD_ROOT/usr/share/sgml

cp -ar dsssl/catalog $RPM_BUILD_ROOT/usr/share/sgml/dsssl/jade
cp -ar dsssl/dsssl.dtd dsssl/style-sheet.dtd dsssl/fot.dtd \
    $RPM_BUILD_ROOT/usr/share/sgml/dsssl/jade

strip $RPM_BUILD_ROOT/usr/bin/*

%post
install-catalog --install dsssl  --version  %{jadever}-%{release}

%preun
install-catalog --remove dsssl   --version  %{jadever}-%{release}

%post -n sp
install-catalog --install sp-html --version %{spver}-%{release}
install-catalog --install unicode --version %{spver}-%{release}

%preun -n sp
install-catalog --remove sp-html --version %{spver}-%{release} 
install-catalog --remove unicode --version %{spver}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc jadedoc/ dsssl/ README COPYING VERSION

%attr(711,root,root) /usr/bin/jade
%attr(755,root,root) /usr/lib/libstyle.so*
%attr(755,root,root) /usr/lib/libgrove.so*
%attr(755,root,root) /usr/lib/libspgrove.so*

%config /usr/share/sgml/dsssl.cat
/usr/share/sgml/dsssl/*

%files -n sp
%defattr(644,root,root,755)
%doc doc/

%attr(711,root,root) /usr/bin/s*
%attr(711,root,root) /usr/bin/nsgmls
%attr(755,root,root) /usr/lib/libsp.so*

%config /usr/share/sgml/sp-html.cat
/usr/share/sgml/html

%config /usr/share/sgml/unicode.cat
/usr/share/sgml/unicode

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
