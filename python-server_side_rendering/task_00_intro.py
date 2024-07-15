import os

def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str):
        print("Erreur : template n'est pas dans le bon format.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : attendees n'est pas dans le bon format.")
        return
    if not template_content:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        invitation = template_content
        try:
            for placeholder, value in attendee.items():
                invitation = invitation.replace(f"{{{placeholder}}}", value if value is not None else "N/A")
            
            output_filename = "output_{}.txt".format(index)
            if os.path.exists(output_filename):
                print("Le fichier {} existe déjà, veuillez vérifier.".format(output_filename))
                continue
            
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(invitation)
        except Exception as e:
            print("Une erreur est survenue lors de la génération de l'invitation pour {}: {}".format(attendee.get('name', 'N/A'), e))
