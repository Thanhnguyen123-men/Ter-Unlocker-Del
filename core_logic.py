import psutil
import os
import shutil
import win32security

def is_ti_owned(path):
    """Kiểm tra xem Owner của file có phải là TrustedInstaller không"""
    try:
        sd = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)
        return "TrustedInstaller" in name
    except Exception:
        return False

def scan_locker(target_path):
    results = []
    if not target_path or not os.path.exists(target_path):
        return results
        
    target_path = os.path.abspath(target_path).lower()
    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] in ["System Idle Process", "System", "Registry"]:
            continue
            
        try:
            p = psutil.Process(proc.info['pid'])
            open_files = p.open_files()
            
            for item in open_files:
                if target_path in item.path.lower():
                    results.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'user': proc.info['username']
                    })
        except (psutil.AccessDenied, psutil.NoSuchProcess, Exception):
            continue
    return results

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.kill()
        return True, f"Killed {pid}"
    except:
        return False, "Failed"

def force_delete(path):
    # CHẶN XÓA NẾU LÀ TRUSTEDINSTALLER
    if is_ti_owned(path):
        return False, "TI_BLOCK"

    try:
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path, ignore_errors=True)
        return True, "Xóa thành công!"
    except Exception as e:
        return False, str(e)