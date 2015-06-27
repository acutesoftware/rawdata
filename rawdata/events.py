#!/usr/bin/python3
# events.py

trend_dicts = [
    {'name':'weekday_sales', 
     'scale':'day_of_week', 
     'trend':{'Mon':0.16, 'Tue':0.14, 'Wed':0.15, 'Thu':0.16, 'Fri':0.2, 'Sat':0.13, 'Sun':.06}
    }, 
    {'name':'xmas_presales', 
     'scale':'day_of_year', 
     'trend':dict([(num + 335, round(0.14 + num*n,3)) 
                     for num, n in enumerate(
                      [0.14/25 for n in range(1, 25)])])
    }, 
]

test_data = [['2015-01-23', 15],
             ['2015-03-11', 75],
             ['2014-05-03', 23],
             ['2015-11-15', 13],
             ['2013-08-15', 45],
            ]

def TEST():
    """
    for d in trend_dicts:
        t = TrendGenerator(d)
        print(t)
    """
    t = TrendGenerator(trend_dicts[0])
    #print(t)
    #print(test_data)
    t_series = t.create_time_series(test_data, 0, 1)
    print(t_series)
        

class TrendGenerator(object):
    """
    Class to build a natural trend of values used by 
    the generator module
    
    Output when printing
    name  = weekday_sales
    scale = day_of_week
    trend = Thu=0.16, Mon=0.16, Sat=0.13, Tue=0.14, Wed=0.15, Fri=0.2, Sun=0.06,

    name  = xmas_presales
    scale = day_of_year
    trend = 335=0.14, 336=0.1456, 337=0.1512, 338=0.1568, 339=0.1624, 340=0.168, 341
    =0.1736, 342=0.1792, 343=0.1848, 344=0.1904, 345=0.196, 346=0.2016, 347=0.2072,
    348=0.2128, 349=0.2184, 350=0.224, 351=0.2296, 352=0.2352, 353=0.2408, 354=0.246
    4, 355=0.252, 356=0.2576, 357=0.2632, 358=0.2688,    
    
    """
    def __init__(self, trend_dict):
        """
        reads a trend dictionary 
        Scale is currently:
            day_of_week
            day_of_year
        """
        self.trend_dict = trend_dict
        
    def __str__(self):
        res = ''
        res += 'name  = ' +  self.trend_dict['name'] + '\n'
        res += 'scale = ' + self.trend_dict['scale'] + '\n'
        res += 'trend = ' 
        for k,v in self.trend_dict['trend'].items():
            if type(k) is str:
                res += k + '='
            else:
                res += str(k) + '='
                
            if type(v) is str:
                res += v + ', '
            else:
                res += str(v) + ', '
        res += '\n'
        return res
        
    def create_time_series(self, lst, date_col_index, val_col_index ):
        """
        use the trend dictionary in the class, take
        the list 'lst' and use the date_col_index to
        modify the val_col_index column according to
        the trend values and type of scale
        """
        mult = 1.0
        for row_num, row in enumerate(lst):
            mult = self._get_mult_for_date(row[date_col_index])
            lst[row_num][val_col_index] = lst[row_num][val_col_index] * mult
        
    def _get_mult_for_date(self, relative_date):
        """ 
        takes a relative_date and finds the multiplier
        based on the scale of the trend
        
        TODO - implement this
        """
        absolute_date = ''
        for k,v in self.trend_dict['trend'].items():
            if self.trend_dict['scale'] == 'day_of_week':
                if absolute_date == relative_date:
                    print('day of week calc: k=', k, 'v = ', v)
        return 1.1  # for testing

if __name__ == '__main__':
    TEST()	
    