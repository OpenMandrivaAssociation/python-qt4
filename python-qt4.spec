%define debug_package %{nil}
%define name2 python2-qt4

Summary:	Set of Python bindings for Trolltech's Qt application framework
Name:		python-qt4
Version:	4.11.2
Release:	2
Group:		Development/KDE and Qt
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	http://garr.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-%{version}/PyQt-x11-gpl-%{version}.tar.gz
Patch2:		03_qreal_float_support.dpatch
BuildRequires:	python-sip >= 1:4.12.2
BuildRequires:	python2-sip >= 1:4.12.2
BuildRequires:	sed
BuildRequires:	qt4-devel >= 3:4.5.1
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	python3-dbus
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(QtAssistantClient)
BuildRequires:	pkgconfig(QtWebKit)
Provides:	PyQt4 = %{version}-%{release}
Requires:	sip-api(%{sip_api_major}) = %{sip_api}
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
PyQt is a set of Python bindings for Trolltech's Qt application framework.

%files

#------------------------------------------------------------

%package core
Summary:	PyQt 4 core
Group:		Development/KDE and Qt

%description core
PyQt 4 core.

%files core
%dir %{py_platsitedir}/PyQt4
%{py_platsitedir}/PyQt4/uic
%{py_platsitedir}/PyQt4/__init__.py
%{py_platsitedir}/PyQt4/pyqtconfig.py
%{py_puresitedir}/dbus/*
%{py_platsitedir}/PyQt4/Qt.so
%{py_platsitedir}/PyQt4/QtCore.so
%{_datadir}/python-sip/PyQt4/Qt
%{_datadir}/python-sip/PyQt4/QtCore
%{qt4dir}/qsci/api/python/PyQt4.api

#------------------------------------------------------------

%package dbus
Summary:	PyQt 4 dbus
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description dbus
PyQt 4 dbus.

%files dbus
%{py_platsitedir}/PyQt4/QtDBus.so
%{_datadir}/python-sip/PyQt4/QtDBus

#------------------------------------------------------------

%package declarative
Summary:	PyQt 4 declarative
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description declarative
PyQt 4 declarative.

%files declarative
%{py_platsitedir}/PyQt4/QtDeclarative.so
%{_datadir}/python-sip/PyQt4/QtDeclarative

#------------------------------------------------------------

%package assistant
Summary:	PyQt 4 assistant
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description assistant
PyQt 4 assistant.

%files assistant
%{py_platsitedir}/PyQt4/QtAssistant.so
%{_datadir}/python-sip/PyQt4/QtAssistant

#------------------------------------------------------------

%package gui
Summary:	PyQt 4 gui
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description gui
PyQt 4 gui.

%files gui
%{py_platsitedir}/PyQt4/QtGui.so
%{_datadir}/python-sip/PyQt4/QtGui

#------------------------------------------------------------

%package network
Summary:	PyQt 4 network
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description network
PyQt 4 network.

%files network
%{py_platsitedir}/PyQt4/QtNetwork.so
%{_datadir}/python-sip/PyQt4/QtNetwork

#------------------------------------------------------------

%package help
Summary:	PyQt 4 help
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description help
PyQt 4 help.

%files help
%{py_platsitedir}/PyQt4/QtHelp.so
%{_datadir}/python-sip/PyQt4/QtHelp

#------------------------------------------------------------

%package opengl
Summary:	PyQt 4 opengl
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description opengl
PyQt 4 opengl.

%files opengl
%{py_platsitedir}/PyQt4/QtOpenGL.so
%{_datadir}/python-sip/PyQt4/QtOpenGL

#------------------------------------------------------------

%package multimedia
Summary:	PyQt 4 multimedia
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description multimedia
PyQt 4 multimedia.

%files multimedia
%{py_platsitedir}/PyQt4/QtMultimedia.so
%{_datadir}/python-sip/PyQt4/QtMultimedia

#------------------------------------------------------------

%package script
Summary:	PyQt 4 script
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description script
PyQt 4 script.

%files script
%{py_platsitedir}/PyQt4/QtScript.so
%{_datadir}/python-sip/PyQt4/QtScript

#------------------------------------------------------------

%package sql
Summary:	PyQt 4 sql
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description sql
PyQt 4 sql.

%files sql
%{py_platsitedir}/PyQt4/QtSql.so
%{_datadir}/python-sip/PyQt4/QtSql

#------------------------------------------------------------

%package svg
Summary:	PyQt 4 svg
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description svg
PyQt 4 svg.

%files svg
%{py_platsitedir}/PyQt4/QtSvg.so
%{_datadir}/python-sip/PyQt4/QtSvg

#------------------------------------------------------------

%package test
Summary:	PyQt 4 test
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description test
PyQt 4 test.

%files test
%{py_platsitedir}/PyQt4/QtTest.so
%{_datadir}/python-sip/PyQt4/QtTest

#------------------------------------------------------------

%package webkit
Summary:	PyQt 4 Webkit
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description webkit
PyQt 4 webkit.

%files webkit
%{py_platsitedir}/PyQt4/QtWebKit.so
%{_datadir}/python-sip/PyQt4/QtWebKit

#------------------------------------------------------------

%package xml
Summary:	PyQt 4 xml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description xml
PyQt 4 xml.

%files xml
%{py_platsitedir}/PyQt4/QtXml.so
%{_datadir}/python-sip/PyQt4/QtXml

#------------------------------------------------------------

%package xmlpatterns
Summary:	PyQt 4 xmlpatterns
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description xmlpatterns
PyQt 4 xmlpatterns.

%files xmlpatterns
%{py_platsitedir}/PyQt4/QtXmlPatterns.so
%{_datadir}/python-sip/PyQt4/QtXmlPatterns

#------------------------------------------------------------

%package scripttools
Summary:	PyQt 4 scripttools
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description scripttools
PyQt 4 scripttools.

%files scripttools
%{py_platsitedir}/PyQt4/QtScriptTools.so
%{_datadir}/python-sip/PyQt4/QtScriptTools

#------------------------------------------------------------

%package designer
Summary:	PyQt 4 designer
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description designer
PyQt 4 designer.

%files designer
%{py_platsitedir}/PyQt4/QtDesigner.so
%{_datadir}/python-sip/PyQt4/QtDesigner

#------------------------------------------------------------

%package phonon
Summary:	PyQt 4 phonon
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{version}

%description phonon
PyQt 4 phonon.

%files phonon
%{py_platsitedir}/PyQt4/phonon.so
%{_datadir}/python-sip/PyQt4/phonon

#------------------------------------------------------------
%package	examples
Summary:	PyQt 4 examples
Group:		Development/KDE and Qt
BuildArch: noarch

%description	examples
PyQt 4 examples

%files		examples
%doc %_docdir/%name/
#------------------------------------------------------------

%package devel
Summary:	PyQt 4 devel
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Requires:	qt4-designer

%description devel
PyQt 4 devel utilities.

%files devel
%{_bindir}/pyuic4
%{_bindir}/pyrcc4
%{_bindir}/pylupdate4
%{qt4plugins}/designer/*

#------------------------------------------------------------
%package -n %{name2}-core
Summary:	PyQt 4 core
Group:		Development/KDE and Qt

%description -n %{name2}-core
Py2Qt 4 core.

%files -n %{name2}-core
%dir %{py2_platsitedir}/PyQt4
%{py2_platsitedir}/PyQt4/uic
%{py2_platsitedir}/PyQt4/__init__.py
%{py2_platsitedir}/PyQt4/pyqtconfig.py
%{py2_puresitedir}/dbus/*
%{py2_platsitedir}/PyQt4/Qt.so
%{py2_platsitedir}/PyQt4/QtCore.so
%{_datadir}/python2-sip/PyQt4/Qt
%{_datadir}/python2-sip/PyQt4/QtCore
#/% {qt4dir}/qsci/api/python/PyQt4.api

#------------------------------------------------------------

%package -n %{name2}-dbus
Summary:	Py2Qt 4 dbus
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-dbus
Py2Qt 4 dbus.

%files -n %{name2}-dbus
%{py2_platsitedir}/PyQt4/QtDBus.so
%{_datadir}/python2-sip/PyQt4/QtDBus

#------------------------------------------------------------

%package -n %{name2}-declarative
Summary:	Py2Qt 4 declarative
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-declarative
Py2Qt 4 declarative.

%files -n %{name2}-declarative
%{py2_platsitedir}/PyQt4/QtDeclarative.so
%{_datadir}/python2-sip/PyQt4/QtDeclarative

#------------------------------------------------------------

%package -n %{name2}-assistant
Summary:	Py2Qt 4 assistant
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-assistant
Py2Qt 4 assistant.

%files -n %{name2}-assistant
%{py2_platsitedir}/PyQt4/QtAssistant.so
%{_datadir}/python2-sip/PyQt4/QtAssistant

#------------------------------------------------------------

%package -n %{name2}-gui
Summary:	Py2Qt 4 gui
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-gui
Py2Qt 4 gui.

%files -n %{name2}-gui
%{py2_platsitedir}/PyQt4/QtGui.so
%{_datadir}/python2-sip/PyQt4/QtGui

#------------------------------------------------------------

%package -n %{name2}-network
Summary:	Py2Qt 4 network
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-network
Py2Qt 4 network.

%files -n %{name2}-network
%{py2_platsitedir}/PyQt4/QtNetwork.so
%{_datadir}/python2-sip/PyQt4/QtNetwork

#------------------------------------------------------------

%package -n %{name2}-help
Summary:	Py2Qt 4 help
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-help
Py2Qt 4 help.

%files -n %{name2}-help
%{py2_platsitedir}/PyQt4/QtHelp.so
%{_datadir}/python2-sip/PyQt4/QtHelp

#------------------------------------------------------------

%package -n %{name2}-opengl
Summary:	Py2Qt 4 opengl
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-opengl
Py2Qt 4 opengl.

%files -n %{name2}-opengl
%{py2_platsitedir}/PyQt4/QtOpenGL.so
%{_datadir}/python2-sip/PyQt4/QtOpenGL

#------------------------------------------------------------

%package -n %{name2}-multimedia
Summary:	Py2Qt 4 multimedia
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-multimedia
Py2Qt 4 multimedia.

%files -n %{name2}-multimedia
%{py2_platsitedir}/PyQt4/QtMultimedia.so
%{_datadir}/python2-sip/PyQt4/QtMultimedia

#------------------------------------------------------------

%package -n %{name2}-script
Summary:	Py2Qt 4 script
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-script
Py2Qt 4 script.

%files -n %{name2}-script
%{py2_platsitedir}/PyQt4/QtScript.so
%{_datadir}/python2-sip/PyQt4/QtScript

#------------------------------------------------------------

%package -n %{name2}-sql
Summary:	Py2Qt 4 sql
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-sql
Py2Qt 4 sql.

%files -n %{name2}-sql
%{py2_platsitedir}/PyQt4/QtSql.so
%{_datadir}/python2-sip/PyQt4/QtSql

#------------------------------------------------------------

%package -n %{name2}-svg
Summary:	Py2Qt 4 svg
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-svg
Py2Qt 4 svg.

%files -n %{name2}-svg
%{py2_platsitedir}/PyQt4/QtSvg.so
%{_datadir}/python2-sip/PyQt4/QtSvg

#------------------------------------------------------------

%package -n %{name2}-test
Summary:	Py2Qt 4 test
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-test
Py2Qt 4 test.

%files -n %{name2}-test
%{py2_platsitedir}/PyQt4/QtTest.so
%{_datadir}/python2-sip/PyQt4/QtTest

#------------------------------------------------------------

%package -n %{name2}-webkit
Summary:	Py2Qt 4 Webkit
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-webkit
Py2Qt 4 webkit.

%files -n %{name2}-webkit
%{py2_platsitedir}/PyQt4/QtWebKit.so
%{_datadir}/python2-sip/PyQt4/QtWebKit

#------------------------------------------------------------

%package -n %{name2}-xml
Summary:	Py2Qt 4 xml
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-xml
Py2Qt 4 xml.

%files -n %{name2}-xml
%{py2_platsitedir}/PyQt4/QtXml.so
%{_datadir}/python2-sip/PyQt4/QtXml

#------------------------------------------------------------

%package -n %{name2}-xmlpatterns
Summary:	Py2Qt 4 xmlpatterns
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-xmlpatterns
Py2Qt 4 xmlpatterns.

%files -n %{name2}-xmlpatterns
%{py2_platsitedir}/PyQt4/QtXmlPatterns.so
%{_datadir}/python2-sip/PyQt4/QtXmlPatterns

#------------------------------------------------------------

%package -n %{name2}-scripttools
Summary:	Py2Qt 4 scripttools
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-scripttools
Py2Qt 4 scripttools.

%files -n %{name2}-scripttools
%{py2_platsitedir}/PyQt4/QtScriptTools.so
%{_datadir}/python2-sip/PyQt4/QtScriptTools

#------------------------------------------------------------

%package -n %{name2}-designer
Summary:	PyQt 4 designer
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-designer
Py2Qt 4 designer.

%files -n %{name2}-designer
%{py2_platsitedir}/PyQt4/QtDesigner.so
%{_datadir}/python2-sip/PyQt4/QtDesigner

#------------------------------------------------------------

%package -n %{name2}-phonon
Summary:	Py2Qt 4 phonon
Group:		Development/KDE and Qt
Requires:	%{name2}-core = %{version}

%description -n %{name2}-phonon
Py2Qt 4 phonon.

%files -n %{name2}-phonon
%{py2_platsitedir}/PyQt4/phonon.so
%{_datadir}/python2-sip/PyQt4/phonon

#------------------------------------------------------------
%package -n	%{name2}-examples
Summary:	Py1Qt 4 examples
Group:		Development/KDE and Qt
BuildArch:	noarch

%description -n %{name2}-examples
Py2Qt 4 examples

%files -n %{name2}-examples
%doc %_docdir/%name2/

#------------------------------------------------------------
# PYTHON 2
%package -n	%{name2}
Summary:	Set of Python3 bindings for Trolltech's Qt application framework
Group:		Development/KDE and Qt
Provides:	python2-qt4 = %version-%release
Provides:	Py2Qt4 = %{version}-%{release}
Requires:	sip-api(%{sip_api_major}) = %{sip_api}
Requires:	%{name2}-core = %{version}
Requires:	%{name2}-dbus = %{version}
Requires:	%{name2}-declarative = %{version}
Requires:	%{name2}-designer = %{version}
Requires:	%{name2}-gui = %{version}
Requires:	%{name2}-help = %{version}
Requires:	%{name2}-multimedia = %{version}
Requires:	%{name2}-network = %{version}
Requires:	%{name2}-opengl = %{version}
Requires:	%{name2}-phonon = %{version}
Requires:	%{name2}-script = %{version}
Requires:	%{name2}-scripttools = %{version}
Requires:	%{name2}-sql = %{version}
Requires:	%{name2}-svg = %{version}
Requires:	%{name2}-test = %{version}
Requires:	%{name2}-webkit = %{version}
Requires:	%{name2}-xml = %{version}
Requires:	%{name2}-xmlpatterns = %{version}

%description -n %{name2}
PyQt is a set of Python2 bindings for Trolltech's Qt application framework

%files -n %{name2}

%prep
%setup -qn PyQt-x11-gpl-%{version}
%apply_patches
cp -a . %{py2dir}

%build
export QTDIR=%{qt4dir}
export PATH=%{qt4dir}/bin:$PATH
export CFLAGS='%{optflags} -fPIC' 
export CXXFLAGS='%{optflags} -fPIC'

%{__python} ./configure.py \
	--qsci-api \
	--confirm-license \
	--sipdir=%{_datadir}/python-sip/PyQt4 \
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

pushd %{py2dir}
%{__python2} ./configure.py \
	--qsci-api \
	--sipdir=%{_datadir}/python2-sip/PyQt4 \
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
# Install Python 3 first, and move aside any executables, to avoid clobbering
# the Python 2 installation:
pushd %{py2dir}
%makeinstall_std INSTALL_ROOT=%{buildroot}
mkdir -p %buildroot%_docdir/%name2
    cp -fr doc/html/* %buildroot%_docdir/%name2/

mkdir %buildroot%_docdir/%name2/examples
    cp -fr examples/* %buildroot%_docdir/%name2/examples/ 

popd

%makeinstall_std INSTALL_ROOT=%{buildroot}
mkdir -p %buildroot%_docdir/%name
    cp -fr doc/html/* %buildroot%_docdir/%name/

mkdir %buildroot%_docdir/%name/examples
    cp -fr examples/* %buildroot%_docdir/%name/examples/ 

# remove Python 3 code from Python 2.6 directory, fixes FTBFS (#564633)
rm -rf %{buildroot}%{python2_sitearch}/PyQt4/uic/port_v3/

# likewise, remove Python 2 code from the Python 3.1 directory:
rm -rf %{buildroot}%{python_sitearch}/PyQt4/uic/port_v2/
