#!/usr/bin/env python
#-*- coding:utf-8 -*-

#---------------------------------------------------------------
# CONNL-U to FoLiA converter
#   by Maarten van Gompel
#   Centre for Language and Speech technology
#   Radboud University Nijmegen
#   proycon AT anaproy DOT nl
#
#   Licensed under GPLv3
#
# This script converts CONNL-U to FoLiA format.
#
#----------------------------------------------------------------

from __future__ import print_function, unicode_literals, division, absolute_import

import sys
import os
import argparse
import conllu
from pynlpl.formats import folia

UPOS_SET = "https://raw.githubusercontent.com/proycon/folia/master/setdefinitions/universal-pos.foliaset.ttl"


def main():
    parser = argparse.ArgumentParser(description="CONLL-U to FoLiA converter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--id',type=str,help="Document ID for the FoLiA document", action='store',default="",required=False)
    parser.add_argument('--lemma-set',dest="lemmaset", type=str,help="URL of the set definition for lemmas", action='store',default="undefined",required=False)
    parser.add_argument('--pos-set',dest="posset",type=str,help="URL of the set definition for language-specific part-of-speech and features (xpos)", action='store',default="undefined",required=False)
    parser.add_argument('--dependency-set',dest="depset", type=str,help="Dependency set", action='store',default="undefined", required=False)
    parser.add_argument('-o', '--outputdir',type=str,help="Output directory", action='store',default=".", required=False)
    parser.add_argument('files', nargs='+', help='CONLL-U input files')
    args = parser.parse_args()


    for file in args.files:
        if args.id:
            doc_id = args.id
        else:
            doc_id = os.path.basename(file)
        doc = None
        hascontent = False
        with open(file,'r',encoding='utf-8') as f:
            sentences = conllu.parse(f.read())
            for i, tokenlist in enumerate(sentences):
                if 'newdoc id' in tokenlist.metadata or i == 0:
                    if doc is not None and hascontent:
                        doc.save(os.path.join(args.outputdir), doc_id + ".folia.xml")
                    if 'newdoc id' in tokenlist.metadata:
                        doc_id = tokenlist.metadata['newdoc id']
                    hascontent = False
                    doc = folia.Document(id=doc_id, autodeclare=True)
                    textbody = folia.Text(doc, id=doc_id+'.text')
                    doc.append(textbody)
                    anchor = textbody
                if 'newpar id' in tokenlist.metadata:
                    anchor = textbody.append(folia.Paragraph, id=tokenlist.metadata['newpar id'])
                if 'sent_id' in tokenlist.metadata:
                    sent_id = tokenlist.metadata['sent_id']
                else:
                    sent_id = doc_id + '.s.' + str(i+1)
                sentence = folia.Sentence(doc, id=sent_id)
                for token in tokenlist:
                    word = sentence.append(folia.Word, token['form'], id=sent_id + ".w." + token['id'])
                    if token['upostag']:
                        pos = word.append(folia.PosAnnotation, cls=token['upostag'], set=UPOS_SET)
                        if token['feats']:
                            for subset, cls in token['feats'].items():
                                pos.append(folia.Feature(subset=subset,cls=cls))
                    if token['xpostag']:
                        word.append(folia.PosAnnotation, cls=token['xpostag'], set=args.posset)
                        if token['feats'] and not token['upostag']:
                            for subset, cls in token['feats'].items():
                                pos.append(folia.Feature(subset=subset,cls=cls))
                    if token['lemma']:
                        word.append(folia.LemmaAnnotation, cls=token['lemma'], set=args.lemmaset)
                    hascontent = True
                anchor.append(sentence)

        if doc is not None and hascontent:
            doc.save(os.path.join(args.outputdir), doc_id + ".folia.xml")





if __name__ == '__main__':
    main()