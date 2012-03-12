Name: python-qt4
Summary: Set of Python bindings for Trolltech's Qt application framework
Version: 4.9.1
Release: %mkrel 1
Group: Development/KDE and Qt
URL: http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0: http://www.riverbankcomputing.co.uk/static/Downloads/PyQt4/PyQt-x11-gpl-%version.tar.gz
Patch2: 03_qreal_float_support.dpatch
License: GPLv2+
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: qt4-devel >= 3:4.5.1
BuildRequires: qt-assistant-adp-devel
BuildRequires: dbus-python
BuildRequires: dbus-devel
BuildRequires: python-sip >= 1:4.12.2
BuildRequires: sed
BuildRequires: phonon-devel
BuildRequires: python-devel
Provides: PyQt4 = %version-%release
Requires: python-sip >= 1:4.12.2
Requires: %{name}-core = %{version}
#Requires: %{name}-assistant = %{version}
Requires: %{name}-dbus = %{version}
Requires: %{name}-declarative = %{version}
Requires: %{name}-designer = %{version}
Requires: %{name}-gui = %{version}
Requires: %{name}-help = %{version}
Requires: %{name}-multimedia = %{version}
Requires: %{name}-network = %{version}
Requires: %{name}-opengl = %{version}
Requires: %{name}-phonon = %{version}
Requires: %{name}-script = %{version}
Requires: %{name}-scripttools = %{version}
Requires: %{name}-sql = %{version}
Requires: %{name}-svg = %{version}
Requires: %{name}-test = %{version}
Requires: %{name}-webkit = %{version}
Requires: %{name}-xml = %{version}
Requires: %{name}-xmlpatterns = %{version}

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework

%files

#------------------------------------------------------------

%package core
Summary: PyQt 4 core
Group: Development/KDE and Qt

%description core
PyQt 4 core

%files core
%defattr(-,root,root)
%dir %py_platsitedir/PyQt4
%py_platsitedir/PyQt4/uic
%py_platsitedir/PyQt4/__init__.py
%py_platsitedir/PyQt4/pyqtconfig.py
%if %mdkversion < 201200
%py_puresitedir/dbus/*
%endif
%py_platsitedir/PyQt4/Qt.so
%py_platsitedir/PyQt4/QtCore.so
%_datadir/sip/PyQt4/Qt
%_datadir/sip/PyQt4/QtCore
%qt4dir/qsci/api/python/PyQt4.api

#------------------------------------------------------------

%package dbus
Summary: PyQt 4 dbus
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description dbus
PyQt 4 dbus

%files dbus
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtDBus.so
%_datadir/sip/PyQt4/QtDBus

#------------------------------------------------------------

%package declarative
Summary: PyQt 4 declarative
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description declarative
PyQt 4 declarative

%files declarative
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtDeclarative.so
%_datadir/sip/PyQt4/QtDeclarative

#------------------------------------------------------------

%package assistant
Summary: PyQt 4 assistant
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description assistant
PyQt 4 assistant

%files assistant
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtAssistant.so
%_datadir/sip/PyQt4/QtAssistant

#------------------------------------------------------------

%package gui
Summary: PyQt 4 gui
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description gui
PyQt 4 gui

%files gui
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtGui.so
%_datadir/sip/PyQt4/QtGui

#------------------------------------------------------------

%package network
Summary: PyQt 4 network
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description network
PyQt 4 network

%files network
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtNetwork.so
%_datadir/sip/PyQt4/QtNetwork

#------------------------------------------------------------

%package help
Summary: PyQt 4 help
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description help
PyQt 4 help

%files help
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtHelp.so
%_datadir/sip/PyQt4/QtHelp

#------------------------------------------------------------

%package opengl
Summary: PyQt 4 opengl
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description opengl
PyQt 4 opengl

%files opengl
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtOpenGL.so
%_datadir/sip/PyQt4/QtOpenGL

#------------------------------------------------------------

%package multimedia
Summary: PyQt 4 multimedia
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description multimedia
PyQt 4 multimedia

%files multimedia
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtMultimedia.so
%_datadir/sip/PyQt4/QtMultimedia

#------------------------------------------------------------

%package script
Summary: PyQt 4 script
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description script
PyQt 4 script

%files script
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtScript.so
%_datadir/sip/PyQt4/QtScript

#------------------------------------------------------------

%package sql
Summary: PyQt 4 sql
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description sql
PyQt 4 sql

%files sql
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtSql.so
%_datadir/sip/PyQt4/QtSql

#------------------------------------------------------------

%package svg
Summary: PyQt 4 svg
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description svg
PyQt 4 svg

%files svg
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtSvg.so
%_datadir/sip/PyQt4/QtSvg

#------------------------------------------------------------

%package test
Summary: PyQt 4 test
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description test
PyQt 4 test

%files test
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtTest.so
%_datadir/sip/PyQt4/QtTest

#------------------------------------------------------------

%package webkit
Summary: PyQt 4 Webkit
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description webkit
PyQt 4 webkit

%files webkit
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtWebKit.so
%_datadir/sip/PyQt4/QtWebKit

#------------------------------------------------------------

%package xml
Summary: PyQt 4 xml
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description xml
PyQt 4 xml

%files xml
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtXml.so
%_datadir/sip/PyQt4/QtXml

#------------------------------------------------------------

%package xmlpatterns
Summary: PyQt 4 xmlpatterns
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description xmlpatterns
PyQt 4 xmlpatterns

%files xmlpatterns
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtXmlPatterns.so
%_datadir/sip/PyQt4/QtXmlPatterns

#------------------------------------------------------------

%package scripttools
Summary: PyQt 4 scripttools
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description scripttools
PyQt 4 scripttools

%files scripttools
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtScriptTools.so
%_datadir/sip/PyQt4/QtScriptTools

#------------------------------------------------------------

%package designer
Summary: PyQt 4 designer
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description designer
PyQt 4 designer

%files designer
%defattr(-,root,root)
%py_platsitedir/PyQt4/QtDesigner.so
%_datadir/sip/PyQt4/QtDesigner


#------------------------------------------------------------

%package phonon
Summary: PyQt 4 phonon
Group: Development/KDE and Qt
Requires: %{name}-core = %{version}

%description phonon
PyQt 4 phonon

%files phonon
%defattr(-,root,root)
%py_platsitedir/PyQt4/phonon.so
%_datadir/sip/PyQt4/phonon


#------------------------------------------------------------

%package devel
Summary: PyQt 4 devel
Group: Development/KDE and Qt
Requires: %{name} = %{version}
Requires: qt4-designer

%description devel
PyQt 4 devel utilities

%files devel
%defattr(-,root,root)
%_bindir/pyuic4
%_bindir/pyrcc4
%_bindir/pylupdate4
%qt4plugins/designer/*

#------------------------------------------------------------

%prep
%setup -qn PyQt-x11-gpl-%version
%patch2 -p1 -b .real

%build
export QTDIR=%qt4dir
export PATH=%qt4dir/bin:$PATH
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

%clean
rm -rf %{buildroot}
