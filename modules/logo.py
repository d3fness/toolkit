class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;33m
 =============================================
  ******ToolKit******ToolKit*********ToolKit**
 =============================================

\033[1;36m =============================================\033[1;m
\033[1;33m|          İşinize yarıyabilicek Hack Tooları        |
\033[1;36m =============================================\033[00m''')

  @classmethod
  def tool_footer(self):
    print('''\033[1;36m_______________________________________________
===============================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mToolKit Şu Anda Yüklenemiyor.\033[1;m
\033[1;31m  [ + ]  \033[1;31mBazı Hatalar Var.\033[1;m
\033[1;31m  [ + ]  \033[1;31mLütfen Daha Sonra Tekrar Deneyiniz.\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[1;33m  [ + ] \033[1;32mTüm Risk Size Aittir.
\033[1;33m  [ + ] \033[1;32mGaranti verilmez.
\033[1;33m  [ + ] \033[1;32mYalnızca yasal amaçla kullanın.
\033[1;33m  [ + ] \033[1;32mEylemlerinizden biz sorumlu değiliz.
\033[1;33m  [ + ] \033[1;32m Yasaklı Şeyler Yapma.

\033[1;31m Toolları yükliyerek tüm koşulları kabul etmiş sayılırsınız.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[1;33m    [ + ] \033[1;32mToolKit Başarıyla Yüklendi.
\033[1;33m    [ + ] \033[1;32mToolKit i Kullanmaya başlıyabilirsiniz =).
\033[1;33m    [ + ] \033[1;32mToolKit i Çalıştırmak İçin Terminale toolKit yada Toolkit Yazın.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[1;33m  [ 1 ] \033[1;32mToolkit i Güncelle.
\033[1;33m  [ 0 ] \033[1;32mGeri dön.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[1;33m      [ + ] \033[1;32mToolKit başarıyla Güncellendi.
\033[1;33m      [ + ] \033[1;32mEnter a basarak devam et.\033[00m''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mİnternet Bağlantısı Var mı?\033[1;m
\033[1;31m  [ + ]  \033[1;31mÇevrimdışı mısınız?\033[1;m
\033[1;31m  [ + ]  \033[1;31mLütfen Daha Sonra Tekrar Deneyiniz.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mToolKit Güncellenemiyor.\033[1;m
\033[1;31m  [ + ]  \033[1;31mLütfen Daha Sonra Tekrar Deneyin.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
\033[1;33m       [+] Yazılım İsmi :- \033[1;32mToolKit
\033[1;33m       [+] Kodlayıcı :- \033[1;32md3fness
\033[1;33m       [+] Son Güncelleme :- \033[1;32m17/9/2021.\033[1;m
\033[1;33m       [+] Toollar :- \033[1;32mtoplam {total} yazılım.\033[1;m

\033[1;33m [+] \033[1;32mToolKit Bir Otomatik Yazılım Yükleyicisidir.
\033[1;33m [+] \033[1;32mTermux Ve Linux İçin Kodlanmıştır.
\033[1;31m [+] Note :- Toolar İle İlgili Tüm Riskler Size Aittir.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[01;33m =============================================
\033[01;32m|_____________ tool seç ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mDikkat !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m Bu Yazılım Zaten Yüklü !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mİşlem Tamamlandı !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m Başarılı Bir Şekilde Yüklendi !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31mÜzgünüm ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m Malesef Yüklenemedi !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\033[01;36m =============================================
\033[01;33m|  00) Geri                                   |
 \033[01;36m=============================================\033[00m""")

  @classmethod
  def updating(self):
    print ("""\033[01;33m =============================================
\033[01;32m|______________ ToolKit Güncelleniyor ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def installing(self):
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Yükleniyor _________________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;33m  [ 1 ] \033[1;32mShow all tools.\033[1;33m [ \033[1;91mAlmost {total} tools\033[1;33m ]
\033[1;33m  [ 2 ] \033[1;32mTool kategorisi.
\033[1;33m  [ 3 ] \033[1;32mToolKit i Güncelle.
\033[1;33m  [ 4 ] \033[1;32mHakkında.
\033[1;33m  [ x ] \033[1;32mÇıkış Yap.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
\033[1;33m         [ + ] \033[1;32mToolKit i Kullandığınız İçin Teşekkür Ederiz
\033[1;33m         [ + ] \033[1;32mBizi Tercih Ettiğiniz İçin Teşekkür Ederim..... :)\033[00m''')
    self.tool_footer()
