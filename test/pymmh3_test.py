# pymmh3 was written by Fredrik Kihlander and enhanced by Swapnil Gusani, and is placed in the public
# domain. The authors hereby disclaim copyright to this source code.

import os
import sys
import unittest
import json

file_dir = os.path.dirname( __file__ )
sys.path.append( os.path.join( file_dir, '..' ) )
import pymmh3

class Testpymmh3( unittest.TestCase ):
    def _load_solutions(self, solution_file, base = 16):
        solution = {}
        with open( os.path.join( file_dir, solution_file ), 'rb' ) as f:
            while True:
                l = f.readline()
                if not l:
                    break
                solution[ l ] = int( f.readline(), base )

        return solution

    def test_32bit_basic_string( self ):
        solution = self._load_solutions('solution_hash32_seed0.txt', 10)

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash( l )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_32bit_basic_bytearray( self ):
        solution = self._load_solutions('solution_hash32_seed0.txt', 10)

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash( bytearray( l ) )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_32bit_custom_seed_string( self ):
        solution = self._load_solutions('solution_hash32_seed1234ABCD.txt', 10)

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash( l, seed = 0x1234ABCD )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_32bit_custom_seed_bytearray( self ):
        solution = self._load_solutions('solution_hash32_seed1234ABCD.txt', 10)

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash( bytearray( l ), seed = 0x1234ABCD )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x86_basic_string( self ):
        solution = self._load_solutions('solution_hash128_x86_seed0.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( l , x64arch = False )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x86_basic_bytearray( self ):
        solution = self._load_solutions('solution_hash128_x86_seed0.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( bytearray( l ), x64arch = False )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x86_custom_seed_string( self ):
        solution = self._load_solutions('solution_hash128_x86_seed1234ABCD.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( l, seed = 0x1234ABCD, x64arch = False )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x86_custom_seed_bytearray( self ):
        solution = self._load_solutions('solution_hash128_x86_seed1234ABCD.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( bytearray( l ), seed = 0x1234ABCD, x64arch = False )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x64_basic_string( self ):
        solution = self._load_solutions('solution_hash128_x64_seed0.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( l, x64arch = True )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x64_basic_bytearray( self ):
        solution = self._load_solutions('solution_hash128_x64_seed0.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( bytearray( l ), x64arch = True )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x64_custom_seed_string( self ):
        solution = self._load_solutions('solution_hash128_x64_seed1234ABCD.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( l, seed = 0x1234ABCD, x64arch = True )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_128bit_x64_custom_seed_bytearray( self ):
        solution = self._load_solutions('solution_hash128_x64_seed1234ABCD.txt')

        with open( os.path.join( file_dir, 'pg1260.txt' ), 'rb' ) as test_file:
            for l in test_file.readlines():
                s = solution[l]
                r = pymmh3.hash128( bytearray( l ), seed = 0x1234ABCD, x64arch = True )
                self.assertEqual( s, r, 'different hash for line: "%s"\n0x%08X != 0x%08X' % ( l, s, r ) )

    def test_hash_string( self ):
        with open( os.path.join( file_dir, 'solution_hash_string.json' ) ) as test_file:
            testcases = json.load(test_file)

        for case in testcases:
            s = case['expected']
            r = pymmh3.hash_string( case['string'] , case['seed'] )
            self.assertEqual( s, r, 'different hash for case: \n0x%08X != 0x%08X' % ( s, r ) )

if __name__ == "__main__":
    unittest.main()
