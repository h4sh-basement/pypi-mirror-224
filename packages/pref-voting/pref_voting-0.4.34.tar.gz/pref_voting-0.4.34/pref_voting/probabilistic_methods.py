'''
    File: voting_methods.py
    Author: Wes Holliday (wesholliday@berkeley.edu) and Eric Pacuit (epacuit@umd.edu)
    Date: June 3, 2023
    
    Implementations of probabilistic voting methods.
'''

from pref_voting.voting_method import  *
import nashpy as nash

@vm(name="Random Dictator")
def random_dictator(profile, curr_cands = None): 
    '''Returns lottery over the candidates that is proportional to the Plurality scores. 

    Args:
        profile (Profile): A Profile object.
        curr_cands (list): A list of candidates to restrict the ranking to. If ``None``, then the ranking is over the entire domain of the profile.

    Returns:
        dict: A dictionary mapping candidates to probabilities.
    ''' 
    
    plurality_scores = profile.plurality_scores(curr_cands = curr_cands)
    total_plurality_scores = sum(list(plurality_scores.values()))

    return {c: plurality_scores[c] / total_plurality_scores for c in plurality_scores.keys()}


@vm(name="Proportional Borda")
def pr_borda(profile, curr_cands=None): 
    '''Returns lottery over the candidates that is proportional to the Borda scores.
    
    Args:   
        profile (Profile): A Profile object.
        curr_cands (list): A list of candidates to restrict the ranking to. If ``None``, then the ranking is over the entire domain of the profile.

    Returns:
        dict: A dictionary mapping candidates to probabilities.
    
    '''
    borda_scores = profile.borda_scores(curr_cands=curr_cands)
    total_borda_scores = sum(list(borda_scores.values()))

    return {c: borda_scores[c] / total_borda_scores for c in borda_scores.keys()}


def _maximal_lottery(edata, curr_cands = None, margin_transformation = lambda x: x):
    '''Implementation of maximal lotteries.   See http://dss.in.tum.de/files/brandt-research/fishburn_slides.pdf 
    
    Returns a list of all maximal lotteries (there may be more than 1)
    '''
    
    A = np.array([[margin_transformation(m) for m in row] 
                  for row in edata.margin_matrix])

    # Create the game
    game = nash.Game(A)
    # Find the Nash Equilibrium with Vertex Enumeration
    equilibria = list(game.vertex_enumeration())
    if len(equilibria) == 0:
        return {c: 1/len(edata.candidates) for c in edata.candidates}
    else:
        eq = random.choice(equilibria)
        return {c: eq[0][cidx] for cidx, c in enumerate(edata.candidates)}

@vm(name="C1 Maximal Lottery")
def c1_maximal_lottery(edata, curr_cands=None): 
    return _maximal_lottery(edata, 
                            curr_cands=curr_cands, 
                            margin_transformation = np.sign)

@vm(name="Maximal Lottery")
def maximal_lottery(edata, curr_cands=None, return_one_lottery = False): 
    
    return _maximal_lottery(edata, 
                            curr_cands=curr_cands, 
                            margin_transformation = lambda x: x)

