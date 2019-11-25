#!bin/bash
sudo apt-get install -y build-essential libcap-dev cmake libboost-all-dev libcapstone-dev gcc-multilib
git clone https://github.com/Z3Prover/z3
cd z3
python -E scripts/mk_make.py --python
cd build
make -j $(nproc)
sudo make install
sudo cp libz3.so /usr/local/

