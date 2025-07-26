import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import qrcode
import time as t1
import rules
import project_3_diabetes_prediction as p3
import os


fig, axs = plt.subplots(2, 2, figsize=(12, 7))
fig.patch.set_facecolor('black')
ax1, ax2, ax3, ax4 = axs.flatten()

fig.suptitle("Medical Report", fontsize=22, color='cyan', fontweight='bold')


img_path = rules.imgg().strip('"')
ax1.axis("off")
if img_path and os.path.exists(img_path):
    img = mpimg.imread(img_path)
    ax1.imshow(img)
else:
    ax1.text(
        0.5, 0.5, "IMAGE\nNOT\nAVAILABLE",
        ha="center", va="center",
        fontsize=12, color="#FFD700"
    )


ax2.axis("off")
ax2.set_facecolor('black')
patient, predictions = p3.predictionn()
patient_stats = rules.stats(patient)
if(predictions==0):
    iop="Low Chances Of Diabetes"
else:
    iop="High Chances Of Diabetes"
ax2.text(
    0.05, 0.95,
    f"PREDICTION:-- {iop}\n =========================== \n PATIENT STATS\n\n{patient_stats}",
    fontsize=12, ha="left", va="top", wrap=True, color="#FFD700"
)


ax3.axis('off')
ax3.set_facecolor('black')
suggestions = rules.generate_patient_report(patient)

ax3.text(
    0.05, 0.95,
    f"===========================\n{suggestions}",
    fontsize=11, ha="left", va="top", wrap=True,
    linespacing=2.0, color="#FFD700"
)


ax4.axis('off')
ax4.set_facecolor('black')

url = "https://www.healthline.com"  
qr_img = qrcode.make(url)
qr_img_path = "qr_code.png"
qr_img.save(qr_img_path)

qr = mpimg.imread(qr_img_path)
ax4.imshow(qr, extent=[0.05, 0.55, 0.35, 0.95])


ax4.text(
    0.6, 0.6,
    "Scan this QR to explore steps,\ndiet plans, and exercises\nfor a healthier lifestyle.",
    fontsize=10, ha="left", va="center", wrap=True, color="#FFD700"
)


dt = t1.asctime()
ax4.text(
    0.05, 0.05,
    f"Report Generated: {dt}",
    fontsize=9, ha="left", color="#FFD700"
)

plt.tight_layout(rect=[0, 0, 1, 0.96])  
plt.show()
