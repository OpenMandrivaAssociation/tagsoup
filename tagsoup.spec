# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define section free
%define gcj_support 0

Name:           tagsoup
Version:        1.2
Release:        %mkrel 0.0.6
Epoch:          0
Summary:        SAX-compliant parser written in Java
License:        GPL
#Vendor:         JPackage Project
#Distribution:   JPackage
Source0:        http://home.ccil.org/~cowan/XML/tagsoup/tagsoup-%{version}-src.zip
URL:            http://mercury.ccil.org/~cowan/XML/tagsoup/
Group:          Development/Java
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
BuildRequires:  java-devel >= 0:1.4.2
%endif
Requires:       jpackage-utils >= 0:1.6
BuildRequires:  ant
BuildRequires:  ant-trax
BuildRequires:  java-rpmbuild >= 0:1.6
BuildRequires:  xalan-j2

%description 
TagSoup is a SAX-compliant parser written in Java that, instead of
parsing well-formed or valid XML, parses HTML as it is found in the wild: nasty
and brutish, though quite often far from short. TagSoup is designed for people
who have to process this stuff using some semblance of a rational application
design. By providing a SAX interface, it allows standard XML tools to be
applied to even the worst HTML.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%build
export CLASSPATH=$(build-classpath xalan-j2-serializer xalan-j2)
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/trax`"
%{ant} \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist docs-api

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc CHANGES README
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0:1.2-0.0.5mdv2011.0
+ Revision: 670661
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.2-0.0.4mdv2011.0
+ Revision: 609170
- rebuild
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:1.2-0.0.2mdv2010.0
+ Revision: 427265
- rebuild

* Wed Jan 09 2008 David Walluck <walluck@mandriva.org> 0:1.2-0.0.1mdv2008.1
+ Revision: 147372
- 1.2
- add gcj post scripts

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.1.3-1.4mdv2008.1
+ Revision: 121028
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 0:1.1.3-1.3mdv2008.0
+ Revision: 87203
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

* Sun Sep 09 2007 Pascal Terjan <pterjan@mandriva.org> 0:1.1.3-1.2mdv2008.0
+ Revision: 82796
- update to new version

* Wed May 16 2007 David Walluck <walluck@mandriva.org> 0:1.1.3-1.1mdv2008.0
+ Revision: 27269
- 1.1.3


* Fri Mar 23 2007 David Walluck <walluck@mandriva.org> 1.0.5-1.1mdv2007.1
+ Revision: 148692
- 1.0.5

* Mon Mar 12 2007 David Walluck <walluck@mandriva.org> 0:1.0.4-1.2mdv2007.1
+ Revision: 142053
- require ant-trax for build
- Import tagsoup

* Mon Mar 12 2007 David Walluck <walluck@mandriva.org> 0:1.0.4-1.1mdv2007.1
- 1.0.4
- release

* Sat Jan 20 2007 Sebastiano Vigna <vigna@dsi.unimi.it> 0:1.0.1-1jpp
- Upgraded to 1.0.1

* Mon Feb 27 2006 Fernando Nasser <fnasser@redhat.com> 0:1.0rc-2jpp
- First JPP 1.7 version

* Fri Jan 28 2005 Sebastiano Vigna <vigna@acm.org> 0:1.0rc-1jpp
- First JPackage version

