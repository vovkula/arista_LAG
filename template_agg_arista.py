#!/usr/bin/env python3

print('-' * 40)

vlan = input('Enter VLAN id: ')
eth = input('Enter interface number: ')
serv = input('Enter connected host: ')

print('\n' + '-' * 40)

with open('arista_lag.txt', 'r') as src, open('arista_cfg.txt', 'w') as dest:
	dest.write((src.read()).format(vlan, eth, serv, 100 + int(eth), 100 + int(eth), serv + ':AGG', vlan, 100 + int(eth)))

with open('arista_cfg.txt', 'r') as dest:
	print(dest.read())

print('-' * 40)

