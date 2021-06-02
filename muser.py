import glob as gl
import os
import tomita.legacy.pysynth as ps

class Muser:
    def generate (self, song, songId, genId):
        for trackIndex, track in enumerate (song):
            ps.make_wav (
                track,
                bpm = 130,
                transpose = 1,
                pause = 0.1,
                boost = 1.15,
                repeat = 0,
                fn = self.getTrackFileName(songId, genId),
            )

        if len(song) > 1:
            ps.mix_files (
                *[self.getTrackFileName (trackIndex) for trackIndex in range (len (song))],
                'song.wav'
            )

            for fileName in gl.glob ('track_*.wav'):
                os.remove (fileName)

    def getTrackFileName (self, trackIndex, genId):
        return f'generations/generation_{genId}/track_{str(1000 + trackIndex)[1:]}.wav'

