enumRelation.py ö�ٸ��ֹ�ϵ
outputFile.py ���뵽�ļ���Ĭ��׷�ӷ�ʽ
outputRelation.py  ������֮��Ĺ�ϵд���ļ�
jiebaCutWords.py �Ͼ�ִ�

todo:
seqWords.py ���������ͳ��
wordFreqUpdate.py ��Ƶͳ��
checkRelation.py ȷ�����������ֹ�ϵ






seg_list = jieba.cut("��ȥ���廪��ѧ�ͱ�����ѧ��")
print("ȫģʽ: " + "/ ".join(seg_list))

# ȫģʽ

seg_list = jieba.cut("��ȥ���廪��ѧ�ͱ�����ѧ��", cut_all=True)
print("ȫģʽ: " + "/ ".join(seg_list))


# ��������ģʽ

seg_list = jieba.cut_for_search("��ȥ���廪��ѧ�ͱ�����ѧ��")
print("��������ģʽ: " + "/ ".join(seg_list))


# ��ȷģʽ/ȫģʽ��-�´ʷ��� �����С�û���ڴʵ��У�Ҳ��HMMģ�� Viterbi�㷨ʶ�����

seg_list = jieba.cut("��ȥ���廪��ѧ�ͱ�����ѧ��",HMM=True)
print("��ȷģʽ/ȫģʽ-�´ʷ���: " + "/ ".join(seg_list))


# ��������ģʽ��-�´ʷ��� �����С�û���ڴʵ��У�Ҳ��HMMģ�� Viterbi�㷨ʶ�����

seg_list = jieba.cut_for_search("��ȥ���廪��ѧ�ͱ�����ѧ��",HMM=True)
print("��������ģʽ-�´ʷ���: " + "/ ".join(seg_list))
