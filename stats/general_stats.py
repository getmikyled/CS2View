from awpy.stats import *
import polars as pl
import dem

if dem.demo is None:
    dem.parse_demo('test.dem')
# dem.parse_demo('test.dem')


def get_adr(player_name=None, side=None):
    '''
    Returns a polars dataframe with columns
        name, side, n_rounds, dmg, adr
        
    ADR:
        ADR is short for Average Damage per Round
    
    Args:
        player_name: name of the player
        side: side to filter by (t, ct, all)
    '''
    if side not in ['t', 'ct', 'all', None]:
        raise ValueError(f'{side} is not a valid option, choose (t, ct, all)')
    
    req_adr = adr(dem.demo)
    req_adr = req_adr.drop('steamid')
    
    if player_name is not None:
        req_adr = req_adr.filter(pl.col('name') == player_name)
    if side is not None:
        req_adr = req_adr.filter(pl.col('side') == side)
    
    return req_adr

def get_kast(player_name=None, side=None, round=None):
    '''
    Returns a polars dataframe with columns
        name, side, kast_rounds, n_rounds, kast
    
    KAST:
        KAST is short for Kills, Assists, Suicides or Trades
        kast_rounds is the number of rounds contributing to KAST
        
    Args:
        player_name: name of the player
        side: side to filter by (t, ct, all)
        round: game round to filter by
    '''
    if side not in ['t', 'ct', 'all', None]:
        raise ValueError(f'{side} is not a valid option, choose (t, ct, all)')

    req_kast = kast(dem.demo)
    req_kast = req_kast.drop('steamid')
    
    if player_name is not None:
        req_kast = req_kast.filter(pl.col('name') == player_name)
    if side is not None:
        req_kast = req_kast.filter(pl.col('side') == side)
    if round is not None:
        req_kast = req_kast.filter(pl.col('n_rounds') == round)
    
    return req_kast
    

def get_rating(player_name=None, side=None, round=None):
    '''
    Returns a polars dataframe with columns
        name, side, n_rounds, impact, rating
        
    Rating:
        Rating is supposed to be one number to summarize how good a player is
        Impact is how impactful someone was during a round
    
    Args:
        player_name: name of the player
        side: side to filter by (t, ct, all)
        round: game round to filter by
    '''
    if side not in ['t', 'ct', 'all', None]:
        raise ValueError(f'{side} is not a valid option, choose (t, ct, all)')
    
    req_rating = rating(dem.demo)
    req_rating = req_rating.drop('steamid')
    
    if player_name is not None:
        req_rating = req_rating.filter(pl.col('name') == player_name)
    if side is not None:
        req_rating = req_rating.filter(pl.col('side') == side)
    if round is not None:
        req_rating = req_rating.filter(pl.col('n_rounds') == round)

    return req_rating


# quick test
if __name__ == '__main__':
    rat = get_rating('ropz')
    print(rat)
    ka = get_kast('ropz')
    print(ka)
    ad = get_adr('ropz')
    print(ad)
