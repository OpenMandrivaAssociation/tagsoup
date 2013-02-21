%define major %(echo %version |cut -d. -f1-2)
Name:           tagsoup
Version:        1.2.1
Release:        1
Epoch:          0
Summary:        SAX-compliant parser written in Java
License:        GPL
Source0:        http://home.ccil.org/~cowan/XML/tagsoup/tagsoup-%{version}-src.zip
URL:            http://mercury.ccil.org/~cowan/XML/tagsoup/
Group:          Development/Java
BuildArch:      noarch
BuildRequires:  java-1.6.0-openjdk-devel
Requires:       jpackage-utils >= 0:1.6
BuildRequires:  ant
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
export JAVA_HOME=%_prefix/lib/jvm/java-1.6.0
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist docs-api

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/lib/%{name}-%{major}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{major}.jar
ln -s %{name}-%{major}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc CHANGES README
%{_javadir}/*.jar

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

