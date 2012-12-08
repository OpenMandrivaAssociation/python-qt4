Name:		python-qt4
Summary:	Set of Python bindings for Trolltech's Qt application framework
Version:	4.9.4
Release:	1
Group:		Development/KDE and Qt
URL:		http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	http://www.riverbankcomputing.co.uk/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz
Patch2:		03_qreal_float_support.dpatch
License:	GPLv2+
BuildRequires:	qt4-devel >= 3:4.5.1
BuildRequires:	qt-assistant-adp-devel
BuildRequires:	dbus-python
BuildRequires:	dbus-devel
BuildRequires:	python-sip >= 1:4.12.2
BuildRequires:	sed
BuildRequires:	phonon-devel
BuildRequires:	python-devel
Provides:	PyQt4 = %{version}-%{release}
Requires:	python-sip >= 1:4.12.2
Requires:	%{name}-core = %{version}
Requires:	%{name}-dbus = %{version}
Requires:	%{name}-declarative = %{version}
Requires:	%{name}-designer = %{version}
Requires:	%{name}-gui = %{version}
Requires:	%{name}-help = %{version}
Requires:	%{name}-multimedia = %{version}
Requires:	%{name}-network = %{version}
Requires:	%{name}-opengl = %{version}
Requires:	%{name}-phonon = %{version}
Requires:	%{name}-script = %{version}
Requires:	%{name}-scripttools = %{version}
Requires:	%{name}-sql = %{version}
Requires:	%{name}-svg = %{version}
Requires:	%{name}-test = %{version}
Requires:	%{name}-webkit = %{version}
Requires:	%{name}-xml = %{version}
Requires:	%{name}-xmlpatterns = %{version}

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework

%files

#------------------------------------------------------------

%package core
Summary:	PyQt 4 core
Group:		Development/KDE and Qt

%description core
PyQt 4 core

%files core
%dir %{py_platsitedir}/PyQt4
%{py_platsitedir}/PyQt4/uic
%{py_platsitedir}/PyQt4/__init__.py
%{py_platsitedir}/PyQt4/pyqtconfig.py
%{py_puresitedir}/dbus/*
%{py_platsitedir}/PyQt4/Qt.so
%{py_platsitedir}/PyQt4/QtCore.so
%{_datadir}/sip/PyQt4/Qt
%{_datadir}/sip/PyQt4/QtCore
%{qt4dir}/qsci/api/python/PyQt4.api

#------------------------------------------------------------

%package dbus
Summary:	PyQt 4 dbus
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description dbus
PyQt 4 dbus

%files dbus
%{py_platsitedir}/PyQt4/QtDBus.so
%{_datadir}/sip/PyQt4/QtDBus

#------------------------------------------------------------

%package declarative
Summary:	PyQt 4 declarative
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description declarative
PyQt 4 declarative

%files declarative
%{py_platsitedir}/PyQt4/QtDeclarative.so
%{_datadir}/sip/PyQt4/QtDeclarative

#------------------------------------------------------------

%package assistant
Summary:	PyQt 4 assistant
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description assistant
PyQt 4 assistant

%files assistant
%{py_platsitedir}/PyQt4/QtAssistant.so
%{_datadir}/sip/PyQt4/QtAssistant

#------------------------------------------------------------

%package gui
Summary:	PyQt 4 gui
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description gui
PyQt 4 gui

%files gui
%{py_platsitedir}/PyQt4/QtGui.so
%{_datadir}/sip/PyQt4/QtGui

#------------------------------------------------------------

%package network
Summary:	PyQt 4 network
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description network
PyQt 4 network

%files network
%{py_platsitedir}/PyQt4/QtNetwork.so
%{_datadir}/sip/PyQt4/QtNetwork

#------------------------------------------------------------

%package help
Summary:	PyQt 4 help
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description help
PyQt 4 help

%files help
%{py_platsitedir}/PyQt4/QtHelp.so
%{_datadir}/sip/PyQt4/QtHelp

#------------------------------------------------------------

%package opengl
Summary:	PyQt 4 opengl
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description opengl
PyQt 4 opengl

%files opengl
%{py_platsitedir}/PyQt4/QtOpenGL.so
%{_datadir}/sip/PyQt4/QtOpenGL

#------------------------------------------------------------

%package multimedia
Summary:	PyQt 4 multimedia
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description multimedia
PyQt 4 multimedia

%files multimedia
%{py_platsitedir}/PyQt4/QtMultimedia.so
%{_datadir}/sip/PyQt4/QtMultimedia

#------------------------------------------------------------

%package script
Summary:	PyQt 4 script
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description script
PyQt 4 script

%files script
%{py_platsitedir}/PyQt4/QtScript.so
%{_datadir}/sip/PyQt4/QtScript

#------------------------------------------------------------

%package sql
Summary:	PyQt 4 sql
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description sql
PyQt 4 sql

%files sql
%{py_platsitedir}/PyQt4/QtSql.so
%{_datadir}/sip/PyQt4/QtSql

#------------------------------------------------------------

%package svg
Summary:	PyQt 4 svg
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description svg
PyQt 4 svg

%files svg
%{py_platsitedir}/PyQt4/QtSvg.so
%{_datadir}/sip/PyQt4/QtSvg

#------------------------------------------------------------

%package test
Summary:	PyQt 4 test
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description test
PyQt 4 test

%files test
%{py_platsitedir}/PyQt4/QtTest.so
%{_datadir}/sip/PyQt4/QtTest

#------------------------------------------------------------

%package webkit
Summary:	PyQt 4 Webkit
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description webkit
PyQt 4 webkit

%files webkit
%{py_platsitedir}/PyQt4/QtWebKit.so
%{_datadir}/sip/PyQt4/QtWebKit

#------------------------------------------------------------

%package xml
Summary:	PyQt 4 xml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description xml
PyQt 4 xml

%files xml
%{py_platsitedir}/PyQt4/QtXml.so
%{_datadir}/sip/PyQt4/QtXml

#------------------------------------------------------------

%package xmlpatterns
Summary:	PyQt 4 xmlpatterns
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description xmlpatterns
PyQt 4 xmlpatterns

%files xmlpatterns
%{py_platsitedir}/PyQt4/QtXmlPatterns.so
%{_datadir}/sip/PyQt4/QtXmlPatterns

#------------------------------------------------------------

%package scripttools
Summary:	PyQt 4 scripttools
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description scripttools
PyQt 4 scripttools

%files scripttools
%{py_platsitedir}/PyQt4/QtScriptTools.so
%{_datadir}/sip/PyQt4/QtScriptTools

#------------------------------------------------------------

%package designer
Summary:	PyQt 4 designer
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description designer
PyQt 4 designer

%files designer
%{py_platsitedir}/PyQt4/QtDesigner.so
%{_datadir}/sip/PyQt4/QtDesigner

#------------------------------------------------------------

%package phonon
Summary:	PyQt 4 phonon
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description phonon
PyQt 4 phonon

%files phonon
%{py_platsitedir}/PyQt4/phonon.so
%{_datadir}/sip/PyQt4/phonon

#------------------------------------------------------------

%package devel
Summary:	PyQt 4 devel
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	qt4-designer

%description devel
PyQt 4 devel utilities

%files devel
%{_bindir}/pyuic4
%{_bindir}/pyrcc4
%{_bindir}/pylupdate4
%{qt4plugins}/designer/*

#------------------------------------------------------------

%prep
%setup -qn PyQt-x11-gpl-%{version}
%patch2 -p1 -b .real

%build
export QTDIR=%{qt4dir}
export PATH=%{qt4dir}/bin:$PATH
export CFLAGS='%{optflags} -fPIC' 
export CXXFLAGS='%{optflags} -fPIC'

python ./configure.py \
	--qsci-api \
	--confirm-license \
	-s /usr/include/dbus-1.0
	
# Some modules not requires X libraries
# Python sip not diferentiate qt modules and always add a X set of 
# libs to link. We're explicitely this unecessary links
# Using same approach to add missin libpython linh

for name in Qt dbus phonon QtAssistant QtCore QtDBus QtDeclarative QtGui QtMultimedia QtNetwork QtOpenGL QtWebKit QtScript QtSvg QtSql QtDesigner QtTest QtXml QtXmlPatterns QtHelp QtScriptTools; do
    if [ -e ${name}/Makefile ]; then
        sed -i "s,^LIBS = ,LIBS = $(python-config --libs) ,g" ${name}/Makefile
	fi
done
sed -i "s,/usr/lib/qt4/include/phonon,/usr/include/phonon,g" phonon/Makefile
sed -i "s,/usr/lib/qt4//include/phonon,/usr/include/phonon,g" phonon/Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall_std INSTALL_ROOT=%{buildroot}

%changelog
* Thu Jun 21 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- Update to 4.9.2

* Mon Mar 12 2012 Lev Givon <lev@mandriva.org> 4.9.1-1mdv2012.0
+ Revision: 784296
- Update to 4.9.1.

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 4.8.4-1
+ Revision: 662313
- new version 4.8.4

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 4.8.3-23
+ Revision: 640291
- rebuild to obsolete old packages

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 4.8.3-22
+ Revision: 636401
- add missing requires

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 4.8.3-1mdv2011.0
+ Revision: 633644
- New version 4.8.3

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 4.8.2-1mdv2011.0
+ Revision: 624592
- new version 4.8.2

* Sat Oct 30 2010 Funda Wang <fwang@mandriva.org> 4.8.1-1mdv2011.0
+ Revision: 590553
- new version 4.8.1

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 4.8-1mdv2011.0
+ Revision: 589912
- new version 4.8

* Sat Oct 09 2010 Funda Wang <fwang@mandriva.org> 4.7.7-2mdv2011.0
+ Revision: 584423
- add upstream patch to fix build pykde

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 4.7.7-1mdv2011.0
+ Revision: 583028
- new version 4.7.7
- versioned requires

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 575000
- new version 4.75

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 4.7.4-3mdv2011.0
+ Revision: 563952
- still build python-assistant but do not promote it as of deprecated module

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 4.7.4-2mdv2011.0
+ Revision: 562058
- rebuild for qt4.7 (assistant not there anymore)

* Wed Jul 14 2010 Funda Wang <fwang@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 552993
- rework link patch
- New version 4.7.4

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 4.7.3-2mdv2010.1
+ Revision: 539596
- rebuild so that shared libraries are properly stripped again

* Sun Apr 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.7.3-1mdv2010.1
+ Revision: 538784
- update to new version 4.7.3

  + Funda Wang <fwang@mandriva.org>
    - link LIBS rather than LDFLAGS

* Thu Mar 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.2-1mdv2010.1
+ Revision: 524982
- Fix file list
- Add patch to fix build against phonon headers
- Add phonon-devel as buildrequires

  + Colin Guthrie <cguthrie@mandriva.org>
    - Fix phonon build by tweaking the Qt-phonon include path to our one and fixing the link libraries.

  + Funda Wang <fwang@mandriva.org>
    - bump req
    - New version 4.7.2

* Thu Jan 21 2010 Funda Wang <fwang@mandriva.org> 4.7-1mdv2010.1
+ Revision: 494592
- add multimedia module
- New version 4.7 final

* Sat Jan 09 2010 Funda Wang <fwang@mandriva.org> 4.7-0.20091231.2mdv2010.1
+ Revision: 488121
- rebuild for new sip

* Fri Jan 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7-0.20091231.1mdv2010.1
+ Revision: 487425
- New snapshot

* Mon Nov 23 2009 Funda Wang <fwang@mandriva.org> 4.6.2-1mdv2010.1
+ Revision: 469306
- new version 4.6.2

* Sat Oct 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.1-1mdv2010.0
+ Revision: 459149
- Update to version 4.6.1 - Bugfix version

* Mon Sep 28 2009 Funda Wang <fwang@mandriva.org> 4.6-1mdv2010.0
+ Revision: 450451
- bump sip requires
- new version 4.6

* Mon Sep 28 2009 Olivier Blin <blino@mandriva.org> 4.5.4-2mdv2010.0
+ Revision: 450313
- fix real implementation on arm & mips since the qreal stuff is
  broken on these arches (from Arnaud Patard, patch from Debian)

* Wed Aug 12 2009 Frederik Himpe <fhimpe@mandriva.org> 4.5.4-1mdv2010.0
+ Revision: 415693
- update to new version 4.5.4

* Wed Jul 15 2009 Funda Wang <fwang@mandriva.org> 4.5.2-1mdv2010.0
+ Revision: 396101
- new version 4.5.2

* Thu Jul 09 2009 Helio Chissini de Castro <helio@mandriva.com> 4.5.1-2mdv2010.0
+ Revision: 393948
- Fix build against new Qt 4.5.2 and proper handle python libraries

* Thu Jun 18 2009 Helio Chissini de Castro <helio@mandriva.com> 4.5.1-1mdv2010.0
+ Revision: 387133
- Bugfix release 4.8.1

* Sat Jun 06 2009 Funda Wang <fwang@mandriva.org> 4.5-1mdv2010.0
+ Revision: 383209
- 4.5 final

* Sat May 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.5-0.20090527.2mdv2010.0
+ Revision: 381218
- Fix file list and link
- Bump release
- New snapshot
- New snapshot
- Versionnate python-sip requires

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.5-0.20090502.1mdv2010.0
+ Revision: 370959
- Fix Build
  Versionnate python-sip
- Update to 4.5 snapshot

* Sun Mar 01 2009 Helio Chissini de Castro <helio@mandriva.com> 4.4.4-6mdv2009.1
+ Revision: 346252
- Fix compilation for 2009.0 and cooker
- Added help module. Added back scintilla

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 4.4.4-2mdv2009.1
+ Revision: 318788
- fix str fmt
- fix spec
- rebuild for new python

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 4.4.4-1mdv2009.1
+ Revision: 301260
- rediff patch
- bump sip req
- new version 4.4.4

* Sat Aug 09 2008 Funda Wang <fwang@mandriva.org> 4.4.3-1mdv2009.0
+ Revision: 270023
- New version 4.4.3
- decrease sip BR
- fix url and source url

* Wed Jul 16 2008 Helio Chissini de Castro <helio@mandriva.com> 4.4.2-2mdv2009.0
+ Revision: 236225
- We have XmlPatterns enabled now in Qt4

* Thu May 22 2008 Funda Wang <fwang@mandriva.org> 4.4.2-1mdv2009.0
+ Revision: 209969
- BR dbus
- New version 4.4.2

  + David Walluck <walluck@mandriva.org>
    - fix PYTHON_LIB setting
    - 4.4-snapshot-20080424

* Tue Feb 19 2008 Thierry Vignaud <tv@mandriva.org> 4.3.3-2mdv2008.1
+ Revision: 173106
- fix percent-in-provides
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 12 2007 Helio Chissini de Castro <helio@mandriva.com> 4.3.3-1mdv2008.1
+ Revision: 117851
- New python qt4 to match kde4 bindings and new qt 4.3.3

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 4.3.1-1mdv2008.1
+ Revision: 109942
- New version 4.3.1
- fix Source url

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 4.3-4mdv2008.0
+ Revision: 68698
- Removed last invalid X requires

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 4.3-3mdv2008.0
+ Revision: 68165
- Fixed test for designer plugin in 64

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 4.3-1mdv2008.0
+ Revision: 68146
- Adde designer plugin
- import python-qt4-4.3-1mdv2008.0

  + David Walluck <walluck@mandriva.org>
    - BuildRequires: python-dbus


