from awpy.stats import *
import polars as pl
import dem

if dem.demo is None:
    dem.parse_demo('test.dem')
# dem.parse_demo('test.dem')
pl.Config.set_tbl_rows(30)  

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

def get_round_stats():
    '''
    Returns a polars dataframe with columns
        Round, Winner, Reason, Bomb Site
    '''
    df = dem.demo.rounds.select([
       pl.col('round_num').alias('Round'), 
       pl.col('winner').alias('Winner'),
       pl.col('reason').alias('Reason'),
       pl.col('bomb_site').alias('Bomb Site'),
    ])
    
    winner = (
        pl.when(pl.col("Winner") == "t") 
          .then(pl.lit("Terrorists"))
        .when(pl.col("Winner") == "ct") 
          .then(pl.lit("Counter‑Terrorists"))
        .otherwise(pl.col("Winner"))
        .alias("Winner")
    )

    reason = (
        pl.when(pl.col("Reason") == "t_killed")
          .then(pl.lit("Terrorists Killed"))
        .when(pl.col("Reason") == "ct_killed")
          .then(pl.lit("Counter‑Terrorists Killed"))
        .when(pl.col("Reason") == "bomb_exploded")
          .then(pl.lit("Bomb Exploded"))
        .otherwise(pl.col("Reason"))
        .alias("Reason")
    )

    bomb_site = (
        pl.when(pl.col("Bomb Site") == "bombsite_a")
          .then(pl.lit("Bombsite A"))
        .when(pl.col("Bomb Site") == "bombsite_b")
          .then(pl.lit("Bombsite B"))
        .when(pl.col("Bomb Site") == "not_planted")
          .then(pl.lit("Not Planted"))
        .otherwise(pl.col("Bomb Site"))
        .alias("Bomb Site")
    )

    return df.with_columns([winner, reason, bomb_site])

def get_player_kills():
    pass
    print(dem.demo.kills.columns)
    return dem.demo.kills


def get_all_players():
    '''
    Returns a tuple of lists
        list 1 has all the members of team1, list2 has all the members of team2
        
    '''
    players = adr(dem.demo)

    players = players.filter(pl.col('side') != 'all')

    full_half = players.filter(pl.col('n_rounds') == 12)

    side_counts = full_half.group_by('side').agg(
        pl.len().alias('num_players')
    )

    team1_side = (
        side_counts.sort('num_players', descending=True)
        .select('side')
        .to_series()
        .to_list()[0]
    )

    team2_side = (
        side_counts.filter(pl.col('side') != team1_side)
        .select('side')
        .to_series()
        .to_list()[0]
    )

    team1_players = (
        full_half.filter(pl.col('side') == team1_side)
        .select('name')
        .unique()
        .to_series()
        .to_list()
    )

    team2_players = (
        full_half.filter(pl.col('side') == team2_side)
        .select('name')
        .unique()
        .to_series()
        .to_list()
    )

    return sorted(team1_players), sorted(team2_players)
    

# quick test
if __name__ == '__main__':
    # rat = get_rating()
    # print(rat)
    # ka = get_kast('ropz')
    # print(ka)
    # ad = get_adr('ropz')
    # print(ad)
    # print(get_player_kills())
    # print(get_all_players())
    print(get_round_stats())
