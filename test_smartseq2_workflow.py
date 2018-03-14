from StepBase import Schedule,Configure
from FastqDump import FastqDump
from Hisat2 import Hisat2
from SamToBam import SamToBam
from BamSort import BamSort
from Cufflinks import Cufflinks
from Cuffmerge import Cuffmerge

Configure.setIdentity('sqchen')

#Fastq-dump
fastq_dump = FastqDump(sraInput1='./minidata/smartseq/sra')

#Hisat2
hisat = Hisat2(ht2Idx="./minidata/smartseq/hg19_index/genome")(fastq_dump)

# Bam2Sam
sam2bam =SamToBam(threads=16)(hisat)

# #BamSort
bamsort = BamSort()(sam2bam)

# #Cufflinks
cufflinks =Cufflinks(gtfInput='./minidata/smartseq/genome.gtf',threads=16)(bamsort)

cuffmerge=Cuffmerge(faInput1='./minidata/smartseq/hg19.fa',gtfInput1='./minidata/smartseq/genome.gtf',threads=16)(cufflinks)

Schedule.run()