from pipeline import process
import os
import time
p_Time = time.time()

# dir_path = r'/media/vkuai/NTFS_Data/AI_Project/AI_EmbeddingVietnameseNLP/corpus/Đời sống.txt'
# with open(dir_path,"r",encoding="utf8") as f:
#     sentences = f.read()
#     print("Read dataset success")
sentences = "Đơn kiện của Loan đã được Toà án quận mười một thụ lý ."
print(process(sentences))
print("Time:", time.time()-p_Time)