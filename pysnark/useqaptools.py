# Portions copyright (C) Meilof Veeningen 2019
#
# Portions copyright (c) 2016-2018 Koninklijke Philips N.V. All rights
# reserved. A copyright license for redistribution and use in source and
# binary forms, with or without modification, is hereby granted for
# non-commercial, experimental and research purposes, provided that the
# following conditions are met:
# - Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimers.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimers in the
#   documentation and/or other materials provided with the distribution. If
#   you wish to use this software commercially, kindly contact
#   info.licensing@philips.com to obtain a commercial license.
#
# This license extends only to copyright and does not include or grant any
# patent license or other license whatsoever.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Copyright (C) Meilof Veeningen, 2019

def privval(val):
    pass
#    pbv=pysnark.libsnark.pb_variable()
#    pbv.allocate(pb)
#    pb.setval(pbv, val)
#    return pysnark.libsnark.linear_combination(pbv)

def pubval(val):
    pass
#    pbv=pysnark.libsnark.pb_variable()
#    pbv.allocate(pb)
#    pb.setpublic(pbv)
#    pb.setval(pbv, val)
#    return pysnark.libsnark.linear_combination(pbv)

def zero():
    pass
#    return pysnark.libsnark.linear_combination()
    
def one():
    pass
#    return pysnark.libsnark.linear_combination(1)

def fieldinverse(val):
    pass
#    return pysnark.libsnark.fieldinverse(val)

def get_modulus():
    pass
#    return pysnark.libsnark.get_modulus()

def add_constraint(v, w, y):
    pass
#    #global comphash
#    
#    pb.add_r1cs_constraint(pysnark.libsnark.r1cs_constraint(v,w,y))
#    
#    #TODO: check, add to hash
#    #comphash = hash((comphash,tuple(v.sig),tuple(w.sig),tuple(y.sig)))
#    #if not libsnark.check_mul(v.value, w.value, y.value):
#    #    raise ValueError()
#    #    needed?
    
def prove():
    pass
#    cs=pb.get_constraint_system_pubs()
#    pubvals=pb.primary_input_pubs();
#    privvals=pb.auxiliary_input_pubs();
#    
#    print("sat", pb.is_satisfied())
#    #print(pysnark.libsnark.r1cs_ppzksnark_generator(cs))
#    keypair=pysnark.libsnark.read_key_or_generate(cs, "pysnark_ek", "pysnark_vk")
#    
#    print("*** PySNARK: generating proof pysnark_log (" +
#          "#io=" + str(pubvals.size()) + 
#          ", #witness=" + str(privvals.size()) + 
#          ", #constraint=" + str(pb.num_constraints()) +
#           ")")
#    
#    proof=pysnark.libsnark.r1cs_ppzksnark_prover(keypair.pk, pubvals, privvals);
#    verified=pysnark.libsnark.r1cs_ppzksnark_verifier_strong_IC(keypair.vk, pubvals, proof);
#    
#    print("*** Public inputs: " + " ".join([str(pubvals.at(i)) for i in range(pubvals.size())]))
#
#    #cerr << "*** Public inputs:";
#    #for (auto &v: pubvals) cerr << " " << v;
#    #cerr << endl;
#    print("*** Verification status:", verified)
    
    

#import os
#import os.path
#import subprocess
#import sys
#
#import options
#import qapsplit
#import qaptools.runqapgen
#import qaptools.runqapgenf
#import qaptools.runqapinput
#import qaptools.runqapprove
#import qaptools.runqapver
#import schedule
#from atexitmaybe import maybe
#
#
#def prove():
#    if options.do_rebuild():
#        qaplens,blklen,extlen,sigs = qapsplit.qapsplit()
#        sz = 1<<((max([max(qaplens.values()),blklen,extlen])-1).bit_length())
#        pubsz = 1<<((extlen-1).bit_length()) if extlen is not None else 0
#        print "qaplen:", max(qaplens.values()), "blklen:", blklen, "extlen:", extlen, "sz", sz, "pubsz", pubsz
#
#        cursz, curpubsz = qaptools.runqapgen.ensure_mkey(sz, pubsz)
#
#        for nm in sigs.keys():
#            qaptools.runqapgenf.ensure_ek(nm, sigs[nm], 1<<((qaplens[nm]-1).bit_length()))
#
#    qaptools.runqapprove.run()
#
#    allfs = list(schedule.oftype("function"))
#    (eqs,eks,vks) = map(set,zip(*[(fn[1], fn[2], fn[3]) for fn in allfs])) if allfs!=[] else (set(),set(), set())
#    alles = list(schedule.oftype("external"))
#    (wrs,cms) = map(set,zip(*[(fn[2], fn[3]) for fn in alles])) if alles!=[] else (set(),set())
#
#    if os.path.isfile(options.get_mpkey_file()) and all([os.path.isfile(vk) for vk in vks]):
#        vercom = qaptools.runqapver.run()
#        print >>sys.stderr, "Verification succeeded"
#    else:
#        vercom = qaptools.runqapver.getcommand()
#        print >>sys.stderr, "Verification keys missing, skipping verification"
#
#    print >>sys.stderr, "  prover keys/eqs: ", options.get_mkey_file(), " ".join(eks), " ".join(eqs), options.get_schedule_file()
#    print >>sys.stderr, "  prover data:     ", " ".join(wrs)
#    print >>sys.stderr, "  verifier keys:   ", options.get_mpkey_file(), " ".join(vks), options.get_schedule_file()
#    print >>sys.stderr, "  verifier data:   ", " ".join(cms), options.get_proof_file(), options.get_io_file()
#    print >>sys.stderr, "  verifier cmd:    ", vercom
#    if options.do_rebuild() and (cursz>sz or curpubsz>pubsz):
#        print >>sys.stderr, "** Evaluation/public keys larger than needed for function: " +\
#                            str(cursz)+">"+str(sz) + " or " + str(curpubsz)+">"+str(pubsz)+ "."
#        print >>sys.stderr, "** To re-create, remove " + options.get_mkey_file() + " and " +\
#                            options.get_mpkey_file() + " and run again."
#
#    #print >>sys.stderr, "  key material + proof material:"
#    #print >>sys.stderr, " ", options.get_mpkey_file(), vks,\
#    #                    options.get_schedule_file(), , bcs
#
#if __name__ == "__main__":
#    prove()
#else:
#    if 'sphinx' not in sys.modules and options.do_pysnark() and options.do_proof():
#        import atexit
#        atexit.register(maybe(prove))
#
#
#from gmpy2 import invert
#import os.path
#
#import options
#import qaptools.runqapgen
#import qaptools.runqapinput
#
#from options import vc_p
#
#import random as rndom
#random = rndom.SystemRandom()
#
#qape = None                # qap equation file (only for key generation)
#qapv = None                # qap wire value file
#qapvo = None
#
#vc_ctx = None
#vc_ctr = dict()
#vc_ioctr = dict()
#
#def init():
#    global qape, qapv, qapvo
#
#    if options.do_pysnark():
#        qapv = open(options.get_wire_file(), "w")
#        print >>qapv, "# PySNARK wire values "
#
#        qapvo = open(options.get_io_file(), "w")
#        print >>qapvo, "# PySNARK i/o"
#
#    if options.do_rebuild():
#        qape = open(options.get_eqs_file(), "w")
#        print >>qape, "# PySNARK equations"
#
#
#def inited(fn):
#    def inited_(*args, **kwargs):
#        if vc_ctx is None:
#            init()
#            enterfn("main", "main")
#        return fn(*args, **kwargs)
#
#    return inited_
#
#
#@inited
#def printwire(sh, nm):
#    if qapv is not None:
#        print >>qapv, nm+":", sh
#        qapv.flush()
#
#@inited
#def printwireout(sh, nm):
#    if qapvo is not None:
#        print >>qapvo, nm+":", sh
#        qapvo.flush()
#
#
#def enterfn(fname, call=None):
#    """
#    Start a new call of the given function type
#    :param fname: Function name. All instances of the same function should execute the exact same sequence of instructions
#    :param call: Call name. Should be globally unique (autogenerated if not given)
#    :return: Call name
#    """
#
#    global vc_ctx, vc_ctr, vc_ioctr
#
#    if vc_ctx is None: init()
#
#    if call is None:
#        call=(vc_ctx+"_"+str(vc_ctr[vc_ctx])+"_" if vc_ctx is not None else "") + fname
#
#    if qape!=None: print >>qape, "[function]", fname, call
#    
#    vc_ctx = call
#    vc_ctr[vc_ctx] = 0
#    vc_ioctr[vc_ctx] = 0
#
#    printwire(random.randint(0, vc_p-1), call+"/deltav") 
#    printwire(random.randint(0, vc_p-1), call+"/deltaw")
#    printwire(random.randint(0, vc_p-1), call+"/deltay")
#
#    printwire(1, call + "/onex")
#    if qape!=None:
#        print >>qape, "* = 1 " + call + "/one -1 " + call + "/onex"
#
#    return call
#
#
#@inited
#def continuefn(call):
#    """
#    Continue execution of the given function call
#    :param call: Function call
#    :return: None
#    """
#    global vc_ctx, vc_ctr
#    vc_ctx = call
#    vc_ctr[vc_ctx] += 1
#
#
#def for_each_in(cls, f, struct):
#    """ Recursively traversing all lists and tuples in struct, apply f to each
#        element that is an instance of cls. Returns structure with f applied. """
#    if isinstance(struct, list):
#        return map(lambda x: for_each_in(cls, f, x), struct)
#    elif isinstance(struct, tuple):
#        return tuple(map(lambda x: for_each_in(cls, f, x), struct))
#    else:
#        if isinstance(struct, cls):
#            return f(struct)
#        else:
#            return struct
#
#
#@inited
#def vc_declare_block(bn, vcs, rnd1=None):
#    global vc_ctx, vc_ctr
#
#    vcs = map(lambda x: x.ensure_single(), vcs)
#    if rnd1 is None: rnd1 = random.randint(0, vc_p-1)
#    printwire(rnd1, vc_ctx+"/rnd1_"+bn)
#    printwire(random.randint(0, vc_p-1), vc_ctx+"/rnd2_"+bn)
#
#    if qape is not None:
#        print >> qape, "[ioblock]", vc_ctx, bn, " ".join(map(lambda x: x.sig[0][1], vcs))
#        qape.flush()
#
#    return vcs
#
#@inited
#def importcomm(bn, nm=None):
#    global vc_ctr, vc_ctx
#    if nm is None:
#        nm = str(vc_ctr[vc_ctx])
#        vc_ctr[vc_ctx] += 1
#
#    fl = options.get_block_file(bn)
#    if not os.path.isfile(fl):
#        raise IOError("Wire file " + fl + " for imported block \"" + bn + "\" does not exist")
#    vals = [int(ln.strip()) for ln in open(fl)]
#    vvals = vc_declare_block(nm, [Var(val,True) for val in vals[:-1]], vals[-1])
#
#    if qape is not None:
#        print >> qape, "[external]", vc_ctx, nm, bn
#        qape.flush()
#
#    return vvals
#
#@inited
#def exportcomm(vals, bn, nm=None):
#    global vc_ctr, vc_ctx
#    if nm is None:
#        nm = str(vc_ctr[vc_ctx])
#        vc_ctr[vc_ctx] += 1
#
#    valsp = [val if isinstance(val, Var) else Var(val,True) for val in vals]
#
#    rnd = random.randint(0,vc_p-1)
#    vc_declare_block(nm, valsp, rnd)
#
#    qaptools.runqapinput.writecomm(bn, [val.value for val in valsp], rnd)
#    qaptools.runqapgen.ensure_mkey(-1, len(vals))
#    qaptools.runqapinput.run(bn)
#
#    if qape != None:
#        print >> qape, "[external]", vc_ctx, nm, bn
#        qape.flush()
#
#    return valsp
#
#
#def vc_glue(ctx1, ctx2, vals):
#    global vc_ctx, vc_ctr
#
#    bakctx = vc_ctx
#
#    rndv = random.randint(0, vc_p - 1)
#
#    vc_ctx = ctx1
#    bn1 = str(vc_ctr[vc_ctx])
#    vc_ctr[vc_ctx] += 1
#    vc_declare_block(bn1, map(lambda x: x[0], vals), rndv)
#
#    vc_ctx = ctx2
#    bn2 = str(vc_ctr[vc_ctx])
#    vc_ctr[vc_ctx] += 1
#    vc_declare_block(bn2, map(lambda x: x[1], vals), rndv)
#
#    vc_ctx = bakctx
#
#    if qape!=None:
#        print >>qape, "[glue]", ctx1, bn1, ctx2, bn2
#        qape.flush()
#
#
#def subqap(nm):
#    def subqap_(fn):
#        @inited
#        def subqap__(*args, **kwargs):
#            global vc_ctx
#
#            if kwargs: raise ValueError("@subqap-decorated functions cannot have keyword arguments")
#
#            oldctx = vc_ctx
#            call = enterfn(nm)
#            newctx = vc_ctx
#
#            argret = []
#
#            def copyandadd(el):
#                ret = Var(el.value, True)
#                argret.append((el, ret))
#                return ret
#
#            def copyandaddrev(el):
#                ret = Var(el.value, True)
#                argret.append((ret, el))
#                return ret
#
#            argscopy = for_each_in(Var, copyandadd, args)
#            ret = fn(*argscopy, **kwargs)
#            continuefn(oldctx)
#            retcopy = for_each_in(Var, copyandaddrev, ret)
#
#            vc_glue(oldctx, newctx, argret)
#
#            return retcopy
#
#        return subqap__
#
#    return subqap_
#
#
#@inited
#def vc_assert_mult(v,w,y):
#    """ Add QAP equation asserting that v*w=y. """
#    if (v.value*w.value-y.value)%vc_p!=0: raise ValueError("QAP equation did not hold")
#
#    if qape!=None:
#        print >>qape, v.strsig(), "*", w.strsig(), "=", y.strsig(), "."
#        qape.flush()
#        
#class Var:
#    """ A variable of the verifiable computation """
#    @inited
#    def __init__(self, val, sig=None):
#        """ Constructor.
#
#        If sig is None, this is an I/O variable with an automatic label.
#        If sig is a string, this is an I/O variable with a given name.
#        If sig is True, this is an internal variable with an automatic label.
#        If sig is anything else, the signature is set to this value.
#        """
#        global vc_ctx, vc_ctr, vc_ioctr
#
#        self.value = val % vc_p
#
#        if sig==None or sig==True or isinstance(sig, str) or isinstance(sig, unicode):
#            vc_ctr[vc_ctx] += 1
#            sid = vc_ctx + "/" + str(vc_ctr[vc_ctx])
#            printwire(val, sid)
#            self.sig = [(1,sid)]
#
#            if sig!=True:
#                if sig==None:
#                    vc_ioctr[vc_ctx] += 1
#                    sido = vc_ctx + "/o_" + str(vc_ioctr[vc_ctx])
#                else:
#                    sido = vc_ctx + "/o_" + sig
#
#                printwireout(val, sido)
#
#                if qape != None:
#                    print >> qape, "*", "= 1", sid, "-1", sido
#                    qape.flush()
#        else:
#            self.sig = sig
#
#        if len(self.sig)>100:
#            vc_ctr[vc_ctx] += 1
#            sid = vc_ctx + "/" + str(vc_ctr[vc_ctx])
#            printwire(val, sid)
#
#            if qape!=None:
#                print >>qape, "*", "=", self.strsig(), "-1", sid
#                qape.flush()
#
#            self.sig = [(1,sid)]
#
#    @classmethod
#    def vars(cls, vals, nm, dim=1):
#        ln = len(str(len(vals)-1))
#        caller = cls if dim==1 else lambda val,nm: cls.vars(val,nm, dim-1)
#        return [caller(val, (nm+"_"+str(ix).zfill(ln))) for (ix,val) in enumerate(vals)]
#
#    @classmethod
#    def vals(cls, vars, nm):
#        ln = len(str(len(vars)-1))
#        return [var.val(nm+"_"+str(ix).zfill(ln)) for (ix,var) in enumerate(vars)]
#
#    def strsig(self):
#        """ Return string representation of linear combination represented by this VcShare. """
#        return " ".join(map(lambda (c,v): str(c)+" "+v, self.sig))
#
#    def __repr__(self):
#        """ Return string representation of this VcShare. """
#        val = self.value if self.value < vc_p/2 else self.value-vc_p
#        return "{" + str(val) + "}"
#        #return "VcShare(" + self.strsig() + (":"+str(self.sh.result) if hasattr(self.sh, 'result') else "") + ")"
#
#    #@inited
#    def ensure_single(self):
#        """ Return a VcShare with the same value that is guaranteed to refer
#            to one witness, by making a new VcShare and adding the required
#            equation if necessary. """
#        if len(self.sig)==1 and self.sig[0][0]==1: return self
#        
#        ret = Var(self.value, True)
#        if qape!=None:
#            print >>qape, "*", "=", self.strsig(), "-1", ret.sig[0][1]
#            qape.flush()
#            
#        return ret
#    
#    @classmethod
#    def zero(cls):
#        """ Return a VcShare representing the value zero. """
#        return Var(0, [])
#    
#    @classmethod
#    @inited
#    def constname(self):
#        return vc_ctx + "/onex"
#    
#    @classmethod
#    def constant(cls, val):
#        """ Return a VcShare representing the given constant value. """
#        return Var(val, [(val % vc_p, cls.constname())])
#
#    @classmethod
#    def random(cls):
#        """ Return a VcShare representing a random value. """
#        return cls(random.randint(0, vc_p-1))
#
#    @classmethod
#    def tovar(cls, val, nm=None):
#        if isinstance(val, Var): return val
#        return Var(val, nm)
#
#    @inited
#    def val(self, nm=None):
#        global vc_ctx, vc_ctr
#        Var(self.value, nm)
#        return self.value
#
#    def __neg__(self):
#        """ Returns negated VcShare. """
#        return Var(vc_p - self.value, [(-c % vc_p, v) for (c, v) in self.sig])
#        
#    def __add__(self, other):
#        """ Add VcShare or constant to self. """
#        if other==0: return self
#        if isinstance(other,int) or isinstance(other,long):
#            return Var((self.value + other) % vc_p, self.sig + [(other, self.constname())])
#        elif isinstance(other, Var):
#            return Var((self.value + other.value) % vc_p, self.sig + other.sig)
#        else:
#            raise TypeError("unsupported operand type(s) for VcShare.+: '{}' and '{}'".format(self.__class__, type(other)))
#    __radd__ = __add__
#            
#    def __sub__(self, other):
#        """ Subtract VcShare or constant from self. """
#        if isinstance(other,int) or isinstance(other,long):
#            return Var((self.value - other) % vc_p, self.sig + [(-other, self.constname())])
#        elif isinstance(other, Var):
#            return self+(-other)
#        else:
#            raise TypeError("unsupported operand type(s) for VcShare.-: '{}' and '{}'".format(self.__class__, type(other)))
#            
#    def __rsub__(self, other):
#        return -self + other
#    
#    def __mul__(self, other):
#        """ Multiply VcShare with other VcShare or constant. """
#        
#        if isinstance(other,int) or isinstance(other,long):
#            return Var((self.value * other) % vc_p, [(c * other % vc_p, v) for (c, v) in self.sig])
#        elif isinstance(other, Var):
#            res = Var((self.value * other.value) % vc_p, True)
#            vc_assert_mult(self, other, res)
#            return res
#        else:
#            return NotImplemented
#
#    __rmul__ = __mul__
#
#    def assert_zero(self):
#        """ Assert that the present VcShare represents the value zero. """
#        if self.value!=0: raise ValueError("nonzero value " + str(self.value))
#
#        if qape!=None:
#            print >>qape, "* =", self.strsig(), "."
#            qape.flush()
#
#    def assert_equals(self, other):
#        (self-other).assert_zero()
#            
#    def assert_nonzero(self):
#        if self.value==0: raise ValueError("zero value")
#
#        inv = Var(long(invert(self.value, vc_p)), True)
#        vc_assert_mult(self, inv, Var.constant(1))
#        
#    def assert_bit(self):
#        """
#        Assert that this variable contains a bit, i.e., 0 or 1
#        :return: None
#        """
#
#        if self.value!=0 and self.value!=1: raise ValueError(str(self.value) + " is not a bit")
#        vc_assert_mult(self, 1 - self, Var.zero())
#            
#    def bit_decompose(self, bl):
#        """ Assert that the present VcShare represents a positive value, that
#            is, a value in [0,2^bl] with bl the given bit length. """
#            
#        bits = [Var((self.value & (1 << i)) >> i, True) for i in xrange(bl)]
#        for i in xrange(len(bits)): vc_assert_mult(bits[i], 1 - bits[i], Var.zero())
#        vc_assert_mult(Var.zero(), Var.zero(), self - sum([(2 ** i) * bits[i] for i in xrange(len(bits))]))
#        return bits
#
#    assert_positive = bit_decompose
#
#    def __div__(self, other):
#        if isinstance(other,int) or isinstance(other,long):
#            otherv = long(invert(other%vc_p, vc_p))
#            return self*otherv
#        else:
#            raise TypeError("unsupported operand type(s) for VcShare./: '{}' and '{}'".format(self.__class__, type(other)))
#
#    def divmod(self, divisor, maxquotbl):
#        """
#        Divide by public value and return quotient and remainder
#        :param divisor: Divisor (integer)
#        :param maxquotbl: Maximal bitlength of the resulting quotient
#        :return: Quotient and remainder
#        """
#        quo = Var(self.value/divisor, True)
#        rem = Var(self.value-quo.value*divisor, True)
#
#        rem.assert_smaller(divisor)
#        quo.assert_positive(maxquotbl)
#
#        (self-divisor*quo-rem).assert_zero()
#        return [quo,rem]
#        
#    def assert_smaller(self, val):
#        if self.value>=val: raise ValueError("value too large: " + str(self.value) + ">=" + str(val))
#        self.bit_decompose(val.bit_length())
#        (val-1-self).bit_decompose(val.bit_length())
#
#    def isnonzero(self):
#        """ Returns VcShare equal to 1 if self is not zero, and 0 if self is zero. """
#
#        eqzs = 1 if self.value != 0 else 0
#        ret = Var(eqzs, True)
#        
#        m = Var(long(invert(self.value + (1 - ret.value), vc_p)), True)
#        
#        if qape!=None:
#            vc_assert_mult(self, m, ret)
#            vc_assert_mult(self, Var.constant(1) - ret, Var.zero())
#                
#        return ret
#
#    def iszero(self):
#        return 1-self.isnonzero()
#
#    def equals(self, other):
#        return (self-other).iszero()