import os
import json
from api.index import app

def run_tests():
    print("=" * 60)
    print("[TEST] Running Tests on StudyMate Vercel Serverless API...")
    print("=" * 60)

    client = app.test_client()

    # 1. Health check
    res = client.get('/health')
    assert res.status_code == 200, f"Health check failed with {res.status_code}"
    print(f"[OK] /health: {res.status_code} -> {res.json.get('status')}")

    # 2. Batches test
    res = client.get('/api/batches')
    assert res.status_code == 200, f"Batches endpoint failed with {res.status_code}"
    batches = res.json
    print(f"[OK] /api/batches: {res.status_code} -> Loaded {len(batches)} batches")

    # 3. Classroom test
    res = client.get('/api/classroom/470')
    assert res.status_code == 200
    classroom = res.json.get('classroom', [])
    print(f"[OK] /api/classroom/470: {res.status_code} -> {len(classroom)} topics")

    # 4. Lesson test
    res = client.get('/api/lesson/4326')
    assert res.status_code == 200
    videos = res.json.get('videos', [])
    print(f"[OK] /api/lesson/4326: {res.status_code} -> {len(videos)} videos")

    # 5. Video test (User course video)
    res = client.get('/api/video/179326')
    assert res.status_code == 200
    vdata = res.json
    assert "hd_video_url" in vdata and "video_url" in vdata and "pdfs" in vdata
    print(f"[OK] /api/video/179326 (KGS live auth): {res.status_code}")
    print(f"   - HD Video URL: {vdata.get('hd_video_url')[:50]}...")
    print(f"   - PDFs: {len(vdata.get('pdfs', []))} items")

    # 6. Video test (StudyMate upstream failover)
    res = client.get('/api/video/140228')
    assert res.status_code == 200
    vdata2 = res.json
    assert "hd_video_url" in vdata2 and "video_url" in vdata2 and "pdfs" in vdata2
    print(f"[OK] /api/video/140228 (StudyMate failover): {res.status_code}")
    print(f"   - HD Video URL: {vdata2.get('hd_video_url')[:50]}...")
    print(f"   - PDFs: {len(vdata2.get('pdfs', []))} items")

    print("=" * 60)
    print("[SUCCESS] ALL TESTS PASSED SUCCESSFULLY! Ready for Vercel deploy.")
    print("=" * 60)

if __name__ == '__main__':
    run_tests()

