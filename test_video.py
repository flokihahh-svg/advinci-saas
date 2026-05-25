from moviepy.editor import VideoFileClip, AudioFileClip

print("🎬 جاري بدء عملية المونتاج البرمجي والرندر... انتظر ثواني")

# 1. استدعاء فيديو الخلفية الـ MOV وملف الصوت الشغال
video_clip = VideoFileClip("background.mov")  # تم التعديل إلى mov لتطابق ملفك!
audio_clip = AudioFileClip("test.mp3")

# 2. دمج الصوت مع الفيديو وقص الفيديو تلقائياً على قد طول الصوت
final_clip = video_clip.set_audio(audio_clip).set_duration(audio_clip.duration)

# 3. تصدير الإعلان النهائي بصيغة mp4 خفيفة ومناسبة للموقع
final_clip.write_videofile(
    "output.mp4", 
    fps=24, 
    codec="libx264", 
    audio_codec="aac"
)

print("🔥 ألف مبروك يا علي! تم رندر الفيديو بنجاح، ابحث عن ملف output.mp4 باليسار")