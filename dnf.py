#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:01:54 2020

@author: charalampos
"""
def DNF(s):
    '''
    Parameters
    ----------
    s : (string) Λογική έκφραση DNF
    x_i : (list) Οι αληθοτιμές που αντιστοιχούν στην λογική έκφραση d.

    Returns
    -------
    str : Ικανοποιείται ή οχι το DNF
    x_i  : (dictionary) Οι αληθοτιμές που ικανοποιούν το DNF.
    '''
    d = s.split('∨')                            # Χωρίζουμε το input string με βάση το σύμβολο διάξευξης
    check = []
    for i in range(len(d)):                     # θα ελέγξουμε αν η λογική πρόταση είναι πάντα ψευδής
        check.append(isAlwaysFalse(d[i]))       # Προσθέτουμε το boolean αποτέλεσμα του ελέγχου στο check
    if check == [True for i in range(len(d))]:  # Εάν όλες οι λογικές προτάσεις είναι πάντα ψευδής
        return 'Όχι'                            # Επιστρέφει Όχι και τερματίζει το πρόγραμμα
 
    ####  Συνεχίζουμε εάν δεν είναι. Αν έστω και μία λογική πρόταση είναι αληθής
    ####  τότε ικανοποιείται το DNF 
    j = check.index(False)                       # Παίρνουμε την θέση τη πρώτης λογικής πρότασης που μπορεί να γίνει True
    x = Fix(d[j])                                # Παίρνουμε το λεξικό των αληθοτιμών που ικανοποιούν την λογική πρόταση d(j)
    variables = s.replace('(','').replace(')','').replace('¬','').replace('∨',' ').replace('∧',' ').split(' ')
    x_i = {}                                     # Φτιάχνουμε το λεξικό στο οποίο θα βάλουμε Αληθοτιμή : Τιμή
    for var in variables:
        x_i[var] = True                          # Βάζουμε όλες τις αληθοτιμές θετικές ( δεν μας ενδιαφέρει )
    x_i.update(x)                                # Ενημερώνουμε τις τιμές του λεξικού x_i με αυτές του x
    return ('Ναι',x_i)

def isAlwaysFalse(d):
    '''
    Parameters
    ----------
    d : (string) Είναι η λογική έκφραση με πράξεις ∧,¬.

    Returns
    -------
    boolean: Εάν οι αληθοτιμές ικανοποιούν την λογική έκφραση
    '''
    d = d.strip('()')                               # Αφαιρούμε τις παρενθέσεις, αν υπάρχουν
    d = d.split('∧')                                # Χωρίζουμε την λογική πρόταση με βάση το σύμβολο σύζευξης
    for i in range(len(d)):                         # Για κάθε στοιχείο της d
        if '¬'+d[i] in d:                           # Eαν υπάρχει η άρνησή του στο d
            return True                             # Επιστρέφει True και σταματάει την επανάληψη
    return False                 

def Fix(d):
    '''
    Parameters
    ----------
    d : (string) Είναι η λογική έκφραση με πράξεις ∧,¬.

    Returns
    -------
    x_i : (dictionary) Λεξικό με key τις αληθοτιμές της έκφρασης d και value την τιμή της κάθε μιας.
    '''
    x_i = {}
    d = d.replace('(','').replace(')','')           # Αφαιρούμε τις παρενθέσεις, αν υπάρχουν
    d = d.split('∧')                                # Χωρίζουμε την λογική πρόταση με βάση το σύμβολο σύζευξης
    for i in range(len(d)):                         # Για κάθε στοιχείο της d
        if '¬' in d[i]:                             # Αν υπάρχει το στοιχείο της άρνησης
            x_i[d[i][1:]] = False                   # Δώσε στην αληθοτιμή d[i][1:] τιμή False
        else:                                       # Αλλιώς
            x_i[d[i]] = True                        # Δώσε στην αληθοτιμή d[i] τιμή True
    return x_i

#### EXAMPLE ####
s = "(x1∧¬x2∧x3)∨(¬x2∧x3)∨(x4∧x5∧¬x6)"
print(DNF(s))
#### Symbols ####
# or  : ∨
# and : ∧
# not : ¬