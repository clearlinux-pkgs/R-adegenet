#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-adegenet
Version  : 2.1.1
Release  : 13
URL      : https://cran.r-project.org/src/contrib/adegenet_2.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/adegenet_2.1.1.tar.gz
Summary  : Exploratory Analysis of Genetic and Genomic Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-adegenet-lib = %{version}-%{release}
Requires: R-LearnBayes
Requires: R-coda
Requires: R-expm
Requires: R-ggplot2
Requires: R-gmodels
Requires: R-gtable
Requires: R-htmltools
Requires: R-httpuv
Requires: R-lazyeval
Requires: R-munsell
Requires: R-permute
Requires: R-pillar
Requires: R-plyr
Requires: R-purrr
Requires: R-reshape2
Requires: R-scales
Requires: R-sf
Requires: R-shiny
Requires: R-spData
Requires: R-spdep
Requires: R-xtable
BuildRequires : R-LearnBayes
BuildRequires : R-ade4
BuildRequires : R-ape
BuildRequires : R-coda
BuildRequires : R-dplyr
BuildRequires : R-expm
BuildRequires : R-ggplot2
BuildRequires : R-gmodels
BuildRequires : R-gtable
BuildRequires : R-htmltools
BuildRequires : R-httpuv
BuildRequires : R-igraph
BuildRequires : R-lazyeval
BuildRequires : R-munsell
BuildRequires : R-permute
BuildRequires : R-pillar
BuildRequires : R-plyr
BuildRequires : R-purrr
BuildRequires : R-reshape2
BuildRequires : R-scales
BuildRequires : R-seqinr
BuildRequires : R-sf
BuildRequires : R-shiny
BuildRequires : R-spData
BuildRequires : R-spdep
BuildRequires : R-vegan
BuildRequires : R-xtable
BuildRequires : buildreq-R

%description
[![Travis-CI Build Status](https://travis-ci.org/thibautjombart/adegenet.png?branch=master)](https://travis-ci.org/thibautjombart/adegenet)

%package lib
Summary: lib components for the R-adegenet package.
Group: Libraries

%description lib
lib components for the R-adegenet package.


%prep
%setup -q -c -n adegenet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552933191

%install
export SOURCE_DATE_EPOCH=1552933191
rm -rf %{buildroot}
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegenet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegenet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library adegenet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  adegenet || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/adegenet/CITATION
/usr/lib64/R/library/adegenet/DESCRIPTION
/usr/lib64/R/library/adegenet/INDEX
/usr/lib64/R/library/adegenet/Meta/Rd.rds
/usr/lib64/R/library/adegenet/Meta/data.rds
/usr/lib64/R/library/adegenet/Meta/features.rds
/usr/lib64/R/library/adegenet/Meta/hsearch.rds
/usr/lib64/R/library/adegenet/Meta/links.rds
/usr/lib64/R/library/adegenet/Meta/nsInfo.rds
/usr/lib64/R/library/adegenet/Meta/package.rds
/usr/lib64/R/library/adegenet/NAMESPACE
/usr/lib64/R/library/adegenet/R/adegenet
/usr/lib64/R/library/adegenet/R/adegenet.rdb
/usr/lib64/R/library/adegenet/R/adegenet.rdx
/usr/lib64/R/library/adegenet/dapcServer/server.R
/usr/lib64/R/library/adegenet/dapcServer/ui.R
/usr/lib64/R/library/adegenet/data/H3N2.rda
/usr/lib64/R/library/adegenet/data/dapcIllus.rda
/usr/lib64/R/library/adegenet/data/datalist
/usr/lib64/R/library/adegenet/data/eHGDP.rda
/usr/lib64/R/library/adegenet/data/hybridtoy.RData
/usr/lib64/R/library/adegenet/data/microbov.rda
/usr/lib64/R/library/adegenet/data/nancycats.rda
/usr/lib64/R/library/adegenet/data/rupica.RData
/usr/lib64/R/library/adegenet/data/sim2pop.rda
/usr/lib64/R/library/adegenet/data/spcaIllus.rda
/usr/lib64/R/library/adegenet/data/swallowtails.rda
/usr/lib64/R/library/adegenet/files/AFLP.txt
/usr/lib64/R/library/adegenet/files/exampleSnpDat.snp
/usr/lib64/R/library/adegenet/files/mondata1.rda
/usr/lib64/R/library/adegenet/files/mondata2.rda
/usr/lib64/R/library/adegenet/files/nancycats.dat
/usr/lib64/R/library/adegenet/files/nancycats.gen
/usr/lib64/R/library/adegenet/files/nancycats.gtx
/usr/lib64/R/library/adegenet/files/nancycats.str
/usr/lib64/R/library/adegenet/files/pdH1N1-HA.fasta
/usr/lib64/R/library/adegenet/files/pdH1N1-NA.fasta
/usr/lib64/R/library/adegenet/files/pdH1N1-data.csv
/usr/lib64/R/library/adegenet/files/swallowtails_loc.csv
/usr/lib64/R/library/adegenet/files/usflu.fasta
/usr/lib64/R/library/adegenet/help/AnIndex
/usr/lib64/R/library/adegenet/help/adegenet.rdb
/usr/lib64/R/library/adegenet/help/adegenet.rdx
/usr/lib64/R/library/adegenet/help/aliases.rds
/usr/lib64/R/library/adegenet/help/paths.rds
/usr/lib64/R/library/adegenet/html/00Index.html
/usr/lib64/R/library/adegenet/html/R.css
/usr/lib64/R/library/adegenet/tests/testthat.R
/usr/lib64/R/library/adegenet/tests/testthat/test-findclust.R
/usr/lib64/R/library/adegenet/tests/testthat/test-prop.R
/usr/lib64/R/library/adegenet/tests/testthat/test-seppop.R
/usr/lib64/R/library/adegenet/tests/testthat/test_accessors.R
/usr/lib64/R/library/adegenet/tests/testthat/test_compoplot.R
/usr/lib64/R/library/adegenet/tests/testthat/test_constructors.R
/usr/lib64/R/library/adegenet/tests/testthat/test_genlight.R
/usr/lib64/R/library/adegenet/tests/testthat/test_haploGen.R
/usr/lib64/R/library/adegenet/tests/testthat/test_hierarchy.R
/usr/lib64/R/library/adegenet/tests/testthat/test_import.R
/usr/lib64/R/library/adegenet/tests/testthat/test_repool.R
/usr/lib64/R/library/adegenet/tests/testthat/test_snapclust.R
/usr/lib64/R/library/adegenet/tests/testthat/test_subset.R
/usr/lib64/R/library/adegenet/tests/testthat/test_summary.R
/usr/lib64/R/library/adegenet/tests/testthat/test_xval.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/adegenet/libs/adegenet.so
/usr/lib64/R/library/adegenet/libs/adegenet.so.avx2
/usr/lib64/R/library/adegenet/libs/adegenet.so.avx512
