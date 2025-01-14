from plotnine import ggplot, coord_fixed, ggtitle, scale_x_continuous
from plotnineseqsuite import geom_alignedSeq, theme_seq, extract
from math import floor, ceil

seqs = ['TTGTGAAAGAC', 'AAGTAAACTAA', 'TAATAAACAAA', 'TAATAAACAAA', 'CTGTAAATATT', 'TAGAAAGGTAT']
result = extract(seqs, start=1, end=4)
a=ggplot() + geom_alignedSeq(data=seqs) + coord_fixed() + theme_seq()+ggtitle('Completed sequences')
b=ggplot() + geom_alignedSeq(data=result) + scale_x_continuous(breaks=lambda x: range(floor(x[0]), ceil(x[1])), labels=lambda x: range(x[0]+1, x[0]+1+len(x)), expand=(0,0)) + coord_fixed() + theme_seq()+ggtitle('Fragmented sequences')
a.save('Fig. complete.png')
b.save('Fig. fragment.png')

from PIL import Image
a_pic=Image.open('Fig. complete.png')
b_pic=Image.open('Fig. fragment.png')
a_width = a_pic.width
a_height = a_pic.height
b_width = b_pic.width
b_height = b_pic.height
dst = Image.new('RGB', (a_width+b_width, b_height), color='white')
dst.paste(a_pic, (0, 0))
dst.paste(b_pic, (a_width, 0))
dst.save('Fig. zoom.png')
