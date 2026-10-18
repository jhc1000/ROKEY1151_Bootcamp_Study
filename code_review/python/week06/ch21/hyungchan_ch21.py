# hyungchan_ch21.py

# 특정 폴더에서 텍스트 파일만 찾아 복사/이동/삭제하는 프로그램
# os, shutil 활용
import os
import shutil

# 1. 특정 폴더에서 모든 .txt 파일을 검색하여 리스트로 반환하는 함수를 작성하시오.
def find_txt_files(folder_path):
    """
    param: folder_path (검색할 폴더 경로)
    return: .txt 파일 경로들의 리스트
    """
    txt_files = []
    if not os.path.exists(folder_path):
        print(f"경로가 존재하지 않습니다: {folder_path}")
        return txt_files
    
    # 해당 폴더 내의 파일들을 검색
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                txt_files.append(file_path)
                
    return txt_files


# 2. 특정 폴더에서 .txt 파일을 찾아 다른 폴더로 복사하는 함수를 작성하시오.
def copy_txt_files(source_folder, destination_folder):
    """
    param: source_folder (원본 폴더 경로)
    param: destination_folder (대상 폴더 경로)
    """
    # 대상 폴더가 없으면 생성
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    txt_files = find_txt_files(source_folder)
    copied_count = 0
    
    for file_path in txt_files:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(destination_folder, filename)
        shutil.copy2(file_path, dest_path)
        print(f"복사 완료: {file_path} -> {dest_path}")
        copied_count += 1
        
    print(f"총 {copied_count}개의 .txt 파일이 복사되었습니다.\n")

# 3. 특정 폴더에서 .txt 파일을 찾아 다른 폴더로 이동하는 함수를 작성하시오.
def move_txt_files(source_folder, destination_folder):
    """
    param: source_folder (원본 폴더 경로)
    param: destination_folder (대상 폴더 경로)
    """
    # 대상 폴더가 없으면 생성
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    txt_files = find_txt_files(source_folder)
    moved_count = 0
    
    for file_path in txt_files:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(file_path, dest_path)
        print(f"이동 완료: {file_path} -> {dest_path}")
        moved_count += 1
        
    print(f"총 {moved_count}개의 .txt 파일이 이동되었습니다.\n")


# 4. 특정 폴더에서 .txt 파일을 찾아 삭제하는 함수를 작성하시오.
def delete_txt_files(destination_folder):
    """
    param: destination_folder (대상 폴더 경로)
    """
    txt_files = find_txt_files(destination_folder)
    deleted_count = 0
    
    for file_path in txt_files:
        os.remove(file_path)
        print(f"삭제 완료: {file_path}")
        deleted_count += 1
        
    print(f"총 {deleted_count}개의 .txt 파일이 삭제되었습니다.\n")


# 5. 앞서 작성한 함수를 호출하여 프로그램을 테스트 하시오.
if __name__ == "__main__":
    # 테스트용 디렉터리 경로 설정
    src_dir = "./ch21/test_source"
    dest_dir = "./ch21/test_destination"
    move_dir = "./ch21/test_move"
    
    # 테스트 환경 초기화 (폴더 및 샘플 파일 생성)
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dest_dir, exist_ok=True)
    
    with open(os.path.join(src_dir, "sample1.txt"), "w", encoding="utf-8") as f:
        f.write("첫 번째 텍스트 파일 내용입니다.")
    with open(os.path.join(src_dir, "sample2.txt"), "w", encoding="utf-8") as f:
        f.write("두 번째 텍스트 파일 내용입니다.")
    with open(os.path.join(src_dir, "document.pdf"), "w", encoding="utf-8") as f:
        f.write("이 파일은 .txt가 아닙니다.")

    print("=== 1. .txt 파일 검색 테스트 ===")
    found_files = find_txt_files(src_dir)
    print(f"검색된 파일 목록: {found_files}\n")
    
    print("=== 2. .txt 파일 복사 테스트 ===")
    copy_txt_files(src_dir, dest_dir)
    
    print("=== 3. .txt 파일 이동 테스트 ===")
    move_txt_files(dest_dir, move_dir)
    
    print("=== 4. .txt 파일 삭제 테스트 ===")
    delete_txt_files(move_dir)
    
    print("모든 테스트가 정상적으로 완료되었습니다.")

print('----------------')


# 특정 폴더 내의 파일을 확장자별로 자동 분류하는 프로그램
# pathlib 활용
from pathlib import Path

# 1. pathlib를 사용하여 특정 폴더 내의 모든 파일 목록을 반환하는 함수를 작성하시오.
def get_all_files(folder_path):
    """
    param: folder_path (검색할 폴더 경로)
    return: 파일 Path 객체들의 리스트
    """
    path = Path(folder_path)
    if not path.exists():
        print(f"경로가 존재하지 않습니다: {folder_path}")
        return []
    
    # 폴더 내의 항목 중 파일(디렉토리 제외)만 리스트로 반환
    file_list = [item for item in path.iterdir() if item.is_file()]
    return file_list

# 2. 특정 폴더 내의 파일을 확장자 별로 폴더를 생성하여 이동하는 함수를 작성하시오.
def organize_files_by_extension(source_folder):
    """
    param: source_folder (정리할 폴더 경로)
    """
    path = Path(source_folder)
    if not path.exists():
        print(f"경로가 존재하지 않습니다: {source_folder}")
        return
    
    # 폴더 내 모든 파일 가져오기
    files = get_all_files(source_folder)
    moved_count = 0
    
    for file_path in files:
        # 확장자 추출 (예: '.txt' -> 'txt', 점 제외)
        ext = file_path.suffix.lower().lstrip('.')
        
        # 확장자가 없는 파일인 경우 예외 처리
        if not ext:
            ext = "no_extension"
            
        # 확장자 이름으로 된 하위 폴더 경로 설정 (예: ./source_folder/txt)
        ext_folder = path / ext
        ext_folder.mkdir(exist_ok=True) # 폴더가 없으면 생성
        
        # 대상 파일 경로 설정 후 이동
        dest_path = ext_folder / file_path.name
        
        # 이미 동일한 이름의 파일이 존재할 경우 충돌 방지 처리 가능 (여기서는 바로 rename)
        file_path.rename(dest_path)
        print(f"이동: {file_path.name} -> [{ext}] 폴더")
        moved_count += 1
        
    print(f"\n총 {moved_count}개의 파일이 확장자별로 분류되었습니다.")

# 3. 앞서 작성한 함수를 호출하여 프로그램을 테스트 하시오.
# 3. 프로그램 테스트
if __name__ == "__main__":
    # 테스트용 디렉터리 경로 설정
    test_dir = Path("./ch21/test_organize_dir")
    test_dir.mkdir(exist_ok=True)
    
    # 테스트를 위한 샘플 파일들 생성
    (test_dir / "document1.txt").write_text("첫 번째 텍스트", encoding="utf-8")
    (test_dir / "document2.txt").write_text("두 번째 텍스트", encoding="utf-8")
    (test_dir / "image.jpg").write_bytes(b"fake jpg bytes")
    (test_dir / "data.csv").write_text("id,name\n1,python", encoding="utf-8")
    (test_dir / "readme").write_text("확장자 없는 파일", encoding="utf-8")
    
    print("=== 1. 파일 목록 조회 테스트 ===")
    files = get_all_files(test_dir)
    for f in files:
        print(f"- {f.name}")
    print()
    
    print("=== 2. 확장자별 폴더 자동 분류 및 이동 테스트 ===")
    organize_files_by_extension(test_dir)