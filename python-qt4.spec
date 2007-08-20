Name: python-qt4
Summary: PyQt is a set of Python bindings for Trolltech's Qt application framework
Version: 4.3
Release: %mkrel 1
Group: Development/KDE and Qt
URL: http://www.riverbankcomputing.co.uk/pyqt/index.php
Source0: http://www.riverbankcomputing.com/Downloads/PyQt3/GPL/PyQt-x11-gpl-%{version}.tar.gz
License: GPL
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: qt4-devel 
BuildRequires: python-dbus
BuildRequires: python-sip >= 1:4.7
%py_requires -d
Provides: PyQt4 = %epoch:%version-%release
Requires: python-sip >= 1:4.7
Requires: %{name}-core = %{version}
Requires: %{name}-assistant = %{version}
Requires: %{name}-designer = %{version}
Requires: %{name}-gui = %{version}
Requires: %{name}-network = %{version}
Requires: %{name}-opengl = %{version}
Requires: %{name}-script = %{version}
Requires: %{name}-sql = %{version}
Requires: %{name}-svg = %{version}
Requires: %{name}-test = %{version}
Requires: %{name}-xml = %{version}

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
%py_puresitedir/dbus/*
%py_platsitedir/PyQt4/Qt.so
%py_platsitedir/PyQt4/QtCore.so
%_datadir/sip/PyQt4/Qt
%_datadir/sip/PyQt4/QtCore

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

%package devel
Summary: PyQt 4 devel
Group: Development/KDE and Qt
Requires: %{name}

%description devel
PyQt 4 devel utilities

%files devel
%defattr(-,root,root)
%_bindir/pyuic4
%_bindir/pyrcc4
%_bindir/pylupdate4

#------------------------------------------------------------

%prep
%setup -q -n PyQt-x11-gpl-%version

%build
export QTDIR=%qt4dir
export PATH=%qt4dir/bin:$PATH
echo "yes" | python ./configure.py 

%make

%install
rm -rf %buildroot
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

