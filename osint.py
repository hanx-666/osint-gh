import requests
import sys
import os

def github_osint(username):
    base_url = f"https://api.github.com/users/{username}"
    
    response = requests.get(base_url)
    
    if response.status_code != 200:
        print(f"Error: Tidak dapat menemukan pengguna '{username}'")
        return

    data = response.json()

    os.system('clear')
    print(f" ")
    print(f"Username: {data.get('login')}")
    print(f"Nama: {data.get('name')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Perusahaan: {data.get('company')}")
    print(f"Lokasi: {data.get('location')}")
    print(f"Email: {data.get('email')}")
    print(f"Blog: {data.get('blog')}")
    print(f"Repositori Publik: {data.get('public_repos')}")
    print(f"Pengikut: {data.get('followers')}")
    print(f"Mengikuti: {data.get('following')}")
    print(f"Profil Dibuat Pada: {data.get('created_at')}")
    print(f"Profil Diperbarui Pada: {data.get('updated_at')}")

    print("\nMengambil daftar repositori publik...")
    repos_response = requests.get(data['repos_url'])

    if repos_response.status_code == 200:
        repos = repos_response.json()
        for repo in repos:
            print(f"- {repo['name']}: {repo['html_url']}")
    else:
        print("Gagal mengambil repositori.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python osint.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    github_osint(username)
