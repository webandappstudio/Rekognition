import boto3

def compare_faces(sourceFile, targetFile):
    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])

def detect_text(self):
    """
    Detects text in the image.

    :return The list of text elements found in the image.
    """
    try:
        response = self.rekognition_client.detect_text(Image=self.image)
        texts = [RekognitionText(text) for text in response['TextDetections']]
        logger.info("Found %s texts in %s.", len(texts), self.image_name)
    except ClientError:
        logger.exception("Couldn't detect text in %s.", self.image_name)
        raise
    else:
        return texts
def main():
    source_file = 'media/source.jpg'
    target_file = 'media/target.jpg'
    face_matches = compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()
