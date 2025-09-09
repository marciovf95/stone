#!/usr/bin/env python3
"""
Script para configurar códigos do AdSense no site
"""
import re
import os

def setup_adsense():
    print("🚀 Configurador de AdSense para Portal PT")
    print("=" * 50)
    
    # Solicita informações do usuário
    publisher_id = input("📝 Digite seu Publisher ID (ca-pub-XXXXXXXXXX): ").strip()
    
    if not publisher_id.startswith('ca-pub-'):
        print("❌ Publisher ID deve começar com 'ca-pub-'")
        return
    
    print("\n📋 Configurando slots de anúncios...")
    
    # Slots para diferentes posições
    slots = {
        'left_sidebar': input("🔹 Slot para sidebar esquerda: ").strip(),
        'right_sidebar': input("🔹 Slot para sidebar direita: ").strip(),
        'bottom_banner': input("🔹 Slot para banner inferior: ").strip()
    }
    
    # Lê o arquivo HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substitui o Publisher ID
    content = content.replace('ca-pub-XXXXXXXXXXXXXXXX', publisher_id)
    
    # Código do AdSense para sidebar
    sidebar_ad_code = f'''<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="{publisher_id}"
     data-ad-slot="{slots['left_sidebar']}"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({{}});
</script>'''
    
    # Código do AdSense para banner
    banner_ad_code = f'''<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="{publisher_id}"
     data-ad-slot="{slots['bottom_banner']}"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({{}});
</script>'''
    
    # Substitui os placeholders
    content = content.replace(
        '''<div class="ad-placeholder">
                    <!-- Aqui vai seu código do AdSense -->
                    <div style="background: var(--bg-tertiary); border: 2px dashed var(--border-color); padding: 20px; text-align: center; color: var(--text-secondary);">
                        <p>📢 AdSense</p>
                        <p style="font-size: 0.8em;">Espaço para anúncio lateral</p>
                        <p style="font-size: 0.7em;">160x600 ou 300x250</p>
                    </div>
                </div>''',
        f'<div class="ad-placeholder">{sidebar_ad_code}</div>'
    )
    
    content = content.replace(
        '''<div class="ad-placeholder">
            <!-- Aqui vai seu código do AdSense -->
            <div style="background: var(--bg-tertiary); border: 2px dashed var(--border-color); padding: 20px; text-align: center; color: var(--text-secondary); margin: 20px 0;">
                <p>📢 AdSense Banner</p>
                <p style="font-size: 0.8em;">Espaço para anúncio horizontal</p>
                <p style="font-size: 0.7em;">728x90 ou 320x50 (mobile)</p>
            </div>
        </div>''',
        f'<div class="ad-placeholder">{banner_ad_code}</div>'
    )
    
    # Salva o arquivo
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✅ AdSense configurado com sucesso!")
    print("📝 Arquivo index.html atualizado")
    print("\n💡 Próximos passos:")
    print("1. Teste o site em http://localhost:8000")
    print("2. Verifique se os anúncios aparecem corretamente")
    print("3. Teste em diferentes tamanhos de tela")
    print("4. Aguarde a aprovação do Google AdSense")

if __name__ == "__main__":
    setup_adsense()
