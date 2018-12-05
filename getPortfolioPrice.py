from nsetools import Nse
nse = Nse()
symbols = ['YESBANK','STRTECH','RAIN','M&M','ASHOKLEY','TATAMOTORS','KOTAKBANK','AKSHOPTFBR','MEGH','MARUTI','BIOCON',
			'BALKRISIND','TRIDENT','BAJAJ-AUTO','AXISBANK','MGL','ITC','MINDACORP','LUPIN','BAJFINANCE','HAVELLS','NIITLTD','MINDTREE','AMBUJACEM','SUNPHARMA']
symbols.sort()
for sym in symbols:
	data = nse.get_quote(sym)
	print("{:10} - {:7} - {:6} - {}".format(sym, data['buyPrice1'],data['pChange'], data['purpose']))