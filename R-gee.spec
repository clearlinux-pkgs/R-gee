#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gee
Version  : 4.13.20
Release  : 1
URL      : https://cran.r-project.org/src/contrib/gee_4.13-20.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gee_4.13-20.tar.gz
Summary  : Generalized Estimation Equation Solver
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gee-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
gee -- solve generalized estimating equations --
an Splus library implementation

%package lib
Summary: lib components for the R-gee package.
Group: Libraries

%description lib
lib components for the R-gee package.


%prep
%setup -q -c -n gee

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584112440

%install
export SOURCE_DATE_EPOCH=1584112440
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gee
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gee
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gee
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gee || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gee/DESCRIPTION
/usr/lib64/R/library/gee/INDEX
/usr/lib64/R/library/gee/Meta/Rd.rds
/usr/lib64/R/library/gee/Meta/features.rds
/usr/lib64/R/library/gee/Meta/hsearch.rds
/usr/lib64/R/library/gee/Meta/links.rds
/usr/lib64/R/library/gee/Meta/nsInfo.rds
/usr/lib64/R/library/gee/Meta/package.rds
/usr/lib64/R/library/gee/NAMESPACE
/usr/lib64/R/library/gee/R/gee
/usr/lib64/R/library/gee/R/gee.rdb
/usr/lib64/R/library/gee/R/gee.rdx
/usr/lib64/R/library/gee/help/AnIndex
/usr/lib64/R/library/gee/help/aliases.rds
/usr/lib64/R/library/gee/help/gee.rdb
/usr/lib64/R/library/gee/help/gee.rdx
/usr/lib64/R/library/gee/help/paths.rds
/usr/lib64/R/library/gee/html/00Index.html
/usr/lib64/R/library/gee/html/R.css
/usr/lib64/R/library/gee/tests/Examples/gee-Ex.Rout.save
/usr/lib64/R/library/gee/tests/data_for_gee_binomial.RData
/usr/lib64/R/library/gee/tests/divergence.R
/usr/lib64/R/library/gee/tests/divergence.Rout.save
/usr/lib64/R/library/gee/tests/testgee.dump
/usr/lib64/R/library/gee/tests/tests.R
/usr/lib64/R/library/gee/tests/tests.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gee/libs/gee.so
/usr/lib64/R/library/gee/libs/gee.so.avx2
/usr/lib64/R/library/gee/libs/gee.so.avx512
